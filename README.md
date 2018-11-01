# README #

将树莓派摄像头的实时画面抓取，对抓取的图片对象调用Google API 模块进行识别，将识别后的画面流化传输到本地网页显示。（由于树莓派只有逻辑和一个摄像头，没有显示屏）



###文件说明###
* Flask_video_stream/
flask-video-streaming_virtual-camera:放置四海皆准的虚拟相机（轮流播放图片），网络源码。camera.py文件
flask-video-streaming-update-pi：修改。开放树莓派摄像头（camera_pi.py文件）。如果是调用其他usb/PC摄像头，则是用camera_opencv.py文件
* Flask_add_google_api.._reall-time/
树莓派摄像头；并且调用Google API做识别。 重点是在camera_opencv.py文件 的处理：image 对象， 数据流化
* 主程序文件
app.py


### How do I get set up? ###
* 1将文件部署到树莓派
* 2链接树莓派和摄像头
* 启动服务
CAMERA=pi/opencv python app.py
* 局域网内的PC 浏览器打开url
