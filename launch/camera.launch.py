from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    video_device_arg = DeclareLaunchArgument(
        'video_device', default_value='/dev/video0', # Udev kuralı yaptıysan '/dev/siha_cam' yap
        description='Kamera portu'
    )
    
    width_arg = DeclareLaunchArgument(
        'width', default_value='640',
        description='Görüntü genişliği'
    )

    height_arg = DeclareLaunchArgument(
        'height', default_value='480',
        description='Görüntü yüksekliği'
    )

    fps_arg = DeclareLaunchArgument(
        'fps', default_value='30.0',
        description='Kare hızı'
    )

    frame_id_arg = DeclareLaunchArgument(
        'frame_id', default_value='camera_link',
        description='TF ağacı için frame ismi'
    )


    video_device = LaunchConfiguration('video_device')
    width = LaunchConfiguration('width')
    height = LaunchConfiguration('height')
    fps = LaunchConfiguration('fps')
    frame_id = LaunchConfiguration('frame_id')

    return LaunchDescription([
        video_device_arg,
        width_arg,
        height_arg,
        fps_arg,
        frame_id_arg,
        
        Node(
            package='siha_camera_pkg',
            executable='camera_publisher',
            name='siha_camera_node',
            output='screen',
            
            
            parameters=[
                {'video_device': video_device},
                {'frame_width': width},
                {'frame_height': height},
                {'frame_rate': fps},
                {'frame_id': frame_id} 
            ],
            
            
            remappings=[
                ('/camera/image_raw', '/siha/camera/image_raw'),
                ('/state', '/siha/state') 
            ]
        )
    ])
