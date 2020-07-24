# xssbot
* xssbot已经集成为docker：[leonsec/xssbot](https://hub.docker.com/r/leonsec/xssbot)
* 该xssbot基于selenium模拟浏览器访问给定页面触发xss
* This XSSBot uses selenium to simulate the browser for access to trigger XSS.
## Environment
* Ubuntu 16.04
* Python 2.7.12
* Google Chrome 84.0.4147.89
## usage
* `xssbot.py`在`/var/xssbot/`
* 修改`xssbot.py`中的url和cookie后
* 使用`python2 xssbot.py`启动即可

* xssbot会访问你给定的url并从该url页面获取需要触发XSS的url然后进行访问，例如:
`http://ip/xssurllist.php`内容如下：
```
<?php
//xssurllist.php
...
$url = "http://xxxx";
//or
$url = $_GET['url'];
echo $url;
...
?>
```
该页面提供用户提交的需要触发xss的url
xssbot提取后会添加你指定的cookie并访问
使用效果：
![](https://s1.ax1x.com/2020/07/24/UjNWod.png)

![](https://s1.ax1x.com/2020/07/24/UjdAR1.png)

> 建议提供url的接口一次提供一个url

* The xssbot will visit a provided url page, such as xssurllist.php
```
<?php
//xssurllist.php
...
$url = "http://xxxx";
//or
$url = $_GET['url'];
echo $url;
...
?>
```
* Then xssbot will extract the url in the webpage and add your custom cookie to visit
