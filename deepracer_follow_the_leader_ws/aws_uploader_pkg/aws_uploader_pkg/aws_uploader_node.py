
import time
import cv2
import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
import boto3
from decimal import Decimal
from deepracer_interfaces_pkg.msg import CameraMsg
                                    
class AwsUploaderNode(Node):
    def __init__(self):
        """Create a ObjectDetectionNode.
        """
        super().__init__('aws_uploader_node')


        # Create subscription to sensor messages from camera.
        self.image_subscriber = self.create_subscription(
            CameraMsg,
            '/camera_pkg/video_mjpeg',
            self.upload_img,
        )
        self.bridge = CvBridge()


    def upload_img(self, sensor_data):
        img = self.bridge.imgmsg_to_cv2(sensor_data[0], desired_encoding='passthrough')  
        path = 'img.png'
        cv2.imwrite('img.png', img)
        region = 'us-east-1'
        client = boto3.client('s3', region_name=region)
        dynamodb = boto3.resource('dynamodb', region_name=region)
        table = dynamodb.Table('Input_Packets')
        response = table.put_item(
            Item={
                'img_path': path,
                'timestamp': Decimal(int(time.time()))
            }
        )
        client.upload_file(path, 'senior-design-images', path)


def main(args=None):
    rclpy.init(args=args)
    aws_uploader_node = AwsUploaderNode()
    rclpy.spin(aws_uploader_node)
    aws_uploader_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
