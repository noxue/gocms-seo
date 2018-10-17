## 使用方法

只能在windows系统下使用，谷歌浏览器必须是v64版本，python2.x版本

* 把谷歌设置为默认浏览器
* 修改server.py中chromedriver的路径
* python server.py 

本项目主要是为 [gocms-ui](https://github.com/noxue/gocms-ui) 项目服务，因为搜索引擎目前不支持获取js动态渲染后的内容，所以借助这个工具，如果是搜索引擎抓取内容，就nginx转发到这个工具上面获取渲染后的内容返回给搜索引擎。

