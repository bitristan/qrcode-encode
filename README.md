qrcode-encode
=============

-qrcode编码的核心代码来自于https://github.com/lincolnloop/python-qrcode，在此基础上添加了部分代码
-另外只保留了PIL，删除了svg生成

使用方法：
1. 将qrcode文件夹作为module导入:
   import qrcode

2. 调用qrcode.make方法生成一张图片，返回结果为PIL的Image对象：
   img = qrcode.make("qrcode content")

3. qrcode.make方法参数说明：
   方法定义：def make(data=None, **kwargs)
   a.其中data为必传参数，为一个字符串，指定二维码编码的内容
   b.剩下的参数以key-value的方式传入，指定其他的一些参数：
     size:指定图片大小，默认为300
     border:指定边框留白的宽度
     is_water:是否液化效果
     is_round:是否圆角效果
     radius:圆角和液化的半径
     fore_color:二维码图片前景色
     back_color:二维码图片背景色
     back_img:二维码背景图片,类型为一个PIL的Image对象
     effect:二维码背景合成的效果，使用此参数back_img不能为空，目前支持'angry_bird','square',None三种效果，其中'angry_bird'需要使用res目录下面的资源图片

4.调用示例可参见一下[qr文件](https://github.com/Tinker-S/qrcode-encode/blob/master/qr)

5.效果如下所列
  
  <img src="https://github.com/Tinker-S/qrcode-encode/blob/master/result/1.png"/>
  
  <img src="https://github.com/Tinker-S/qrcode-encode/blob/master/result/2.png"/>
  
  <img src="https://github.com/Tinker-S/qrcode-encode/blob/master/result/3.png"/>
  
  <img src="https://github.com/Tinker-S/qrcode-encode/blob/master/result/4.png"/>
  
  <img src="https://github.com/Tinker-S/qrcode-encode/blob/master/result/5.png"/>
  
  <img src="https://github.com/Tinker-S/qrcode-encode/blob/master/result/6.png"/>
  
  <img src="https://github.com/Tinker-S/qrcode-encode/blob/master/result/7.png"/>
  
  <img src="https://github.com/Tinker-S/qrcode-encode/blob/master/result/angrybird.png"/>
