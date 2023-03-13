
#  📽 **Convert Video to Audio** 🔊
## Using Thread 🧶🧵
+

> + in this program , we want to convert videos into audios , in 2 ways :
> 1. normal converting with 'normal_execution' method
> 2. convert files using 'Thread'

## Requirements :
first you have to install moviepy :
> + pip install movipy
then import it in the code .

second , you need to install & import 'requests' :
>   pip install requests
> + Requests is a simple, HTTP library that allows you to send HTTP requests using Python.
> + Allows you to send HTTP/1.1 PUT, DELETE, HEAD, GET and OPTIONS requests

third , For the creation of a thread, we will use the threading module.
> import threading
+

## Result 
> execution time for 5 vodeo files ,with normal converting was : 
> + 13.32 seconds
> and execution time using Multi-Treading was :
> + 5.7 seconds 
as shown in the below image :

![This is an image](https://github.com/kiana-jahanshid/pylearn/blob/master/Assignment_24/video_into_audio/report.jpg)
+
+
# conclusion : 
> + if you want to speed up "specific operations" in some parts of your code , you can use threading.

