import rclpy
import serial

from rclpy.node import Node
from sensor_msgs.msg import Range


def string_parser(string):
    # format = "%f,%f,%d,%d"
    arr = string.strip().split(',')
    f1 = float(arr[0].strip())
    f2 = float(arr[1].strip())
    f3 = float(arr[2].strip())
    f4 = float(arr[3].strip())
    d1 = int(arr[4].strip())
    d2 = int(arr[5].strip())
    d3 = int(arr[6].strip())
    return f1, f2, f3, f4, d1, d2, d3


class PySerialNode(Node):

    def __init__(
        self,
        name='PySerial_Node',
    ):
        super().__init__(name)

        self.declare_parameter('topic', f'/serial/{name}')

        self.declare_parameter('port', '/dev/pts/3')
        self.declare_parameter('baudrate', 115200)

        topic = str(self.get_parameter('topic').value)

        port = str(self.get_parameter('port').value)
        baudrate = int(self.get_parameter('baudrate').value)
        serial_time_period = 0.01

        self.serial = serial.Serial(port=port, baudrate=baudrate)
        self.serial_timer = self.create_timer(serial_time_period,
                                              self.serial_read_callback)

        self.get_logger().info(
            f'Connected to serial port "{port}" with baudrate {baudrate}.')
        self.get_logger().info(
            f'Receiving data from serial port "{port}" every {serial_time_period}s.'
        )

        self.range_publisher_1 = self.create_publisher(Range, '/range_1', 10)
        self.range_publisher_2 = self.create_publisher(Range, '/range_2', 10)
        range_timer_period = 0.1
        self.range_timer = self.create_timer(range_timer_period,
                                             self.range_timer_callback)

        self.data_buffer = []
        self.data_bufflen = 10

    def serial_read_callback(self):
        if self.serial.in_waiting > 0:
            self.get_logger().info(f'serial got new data')
            data_str = self.serial.readline().decode()
            try:
                arr = string_parser(data_str)
                if len(self.data_buffer) <= self.data_bufflen:
                    self.data_buffer.append(data_str)
                    arr_str = [f'\n data[{i}]: {x}' for i, x in enumerate(arr)]
                    self.get_logger().info(f'Received: serial data {data_str}')
                    print(*arr_str, '\n\n')
                else:
                    self.get_logger().warning('Serial data buffer overflowed!')
            except:
                self.get_logger().info(f'serial read: {data_str}')

    def range_timer_callback(self):
        if len(self.data_buffer) > 0:
            data = self.data_buffer.pop(0)
            f1, f2, f3, f4, d1, d2, d3 = string_parser(data)

            timestamp = self.get_clock().now().to_msg()

            range_1 = Range()
            range_1.header.stamp = timestamp
            range_1.radiation_type = 0
            range_1.min_range = 3.0
            range_1.max_range = 200.0
            range_1.range = f1

            range_2 = Range()
            range_2.header.stamp = timestamp
            range_2.radiation_type = 0
            range_2.min_range = 3.0
            range_2.max_range = 200.0
            range_2.range = f2

            self.range_publisher_1.publish(range_1)
            self.range_publisher_2.publish(range_2)


def main(args=None):
    try:
        rclpy.init(args=args)
        node = PySerialNode('GetSensor_Node')
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
