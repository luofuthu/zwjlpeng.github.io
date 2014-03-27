Date: 2014-03-25
Title: Communications link failure due to underlying exception
Category: 编程语言
Tags: Java分析
Slug: jdbc
Img:pics/java.jpg
summary:从上面的代码中可以看出的是jdbc成功的向远程服务器发送了请求的报文，但是远程服务器拒绝了对该报文进行回复,配置`mysql`数据库，默认情况下msyql默认的,`mysql`只能接受localhost的访问，因此如果如用户想开放远程访问的话，就必须禁用掉bind-address项,则bind-address应该设置成如下形式,或者采用将bind-address设置...

----------
如下是通过捕捉异常打印出调用的堆栈信息显示的错误信息如下：

	com.mysql.jdbc.CommunicationsException: Communications link failure due to underlying exception: 
	
	** BEGIN NESTED EXCEPTION ** 
	
	java.net.ConnectException
	MESSAGE: Connection refused: connect
	
	STACKTRACE:
	
	java.net.ConnectException: Connection refused: connect
		at java.net.TwoStacksPlainSocketImpl.socketConnect(Native Method)
		at java.net.AbstractPlainSocketImpl.doConnect(AbstractPlainSocketImpl.java:337)
		at java.net.AbstractPlainSocketImpl.connectToAddress(AbstractPlainSocketImpl.java:198)
		at java.net.AbstractPlainSocketImpl.connect(AbstractPlainSocketImpl.java:180)
		at java.net.PlainSocketImpl.connect(PlainSocketImpl.java:157)
		at java.net.SocksSocketImpl.connect(SocksSocketImpl.java:391)
		at java.net.Socket.connect(Socket.java:579)
		at java.net.Socket.connect(Socket.java:528)
		at java.net.Socket.<init>(Socket.java:425)
		at java.net.Socket.<init>(Socket.java:241)
		at com.mysql.jdbc.StandardSocketFactory.connect(StandardSocketFactory.java:256)
		at com.mysql.jdbc.MysqlIO.<init>(MysqlIO.java:271)
		at com.mysql.jdbc.Connection.createNewIO(Connection.java:2744)
		at com.mysql.jdbc.Connection.<init>(Connection.java:1553)
		at com.mysql.jdbc.NonRegisteringDriver.connect(NonRegisteringDriver.java:285)
		at java.sql.DriverManager.getConnection(DriverManager.java:579)
		at java.sql.DriverManager.getConnection(DriverManager.java:221)
		at DB.main(DB.java:13)
	
	
	`** END NESTED EXCEPTION **`
	
	
	
	Last packet sent to the server was 0 ms ago.
		at com.mysql.jdbc.Connection.createNewIO(Connection.java:2820)
		at com.mysql.jdbc.Connection.<init>(Connection.java:1553)
		at com.mysql.jdbc.NonRegisteringDriver.connect(NonRegisteringDriver.java:285)
		at java.sql.DriverManager.getConnection(DriverManager.java:579)
		at java.sql.DriverManager.getConnection(DriverManager.java:221)
		at DB.main(DB.java:13)



从上面的代码中可以看出的是jdbc成功的向远程服务器发送了请求的报文，但是远程服务器拒绝了对该报文进行回复


**解决方法** 

配置mysql数据库，默认情况下msyql默认的bind-address是127.0.0.1，mysql只能接受localhost的访问，因此如果如用户想开放远程访问的话，就必须禁用掉bind-address项

**禁用的方法**

    bind-address = 0.0.0.0


**或者采用将bind-address设置为本机ip地址**

假设我本机的`ip`地址为`192.168.161.197`

则bind-address应该设置成如下形式

    bind-address=192.168.161.197

**备注**

mysql中配置文件的位置为安装目录下的`my.ini`或者`my.conf`文件，修改时直接将配置项添加在文件末尾即可



