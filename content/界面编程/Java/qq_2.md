Date: 2013-12-01
Title:界面编程模仿篇(QQ登录界面逼真篇) 
Category: 玩转技术
Tags:界面编程 
Slug: qqLogin_1
Img:pics/tech/QQ_7.jpg
summary:**对JPasswordField的处理**，QQ密码限制了长度，而且禁止了copy,paste,cut,以及对文本的选择操作，在这里就要自已实现一个类继承JPasswordFiled,在这个类里面重写copy,paste,cut,同时还得重写`JPasswordField`的Document模型对像，只有重写了它，才能限制密码的输入长度，以下是限制密码长度的代码。

写了好多天的爬虫，偷空前前后后用了两天的时间(排除吃饭睡觉)写完了这个QQ登录界面，看起来还凑和着吧，如果是的大神的，莫见笑，纯属业余作品，废话先不多说，截图如下,其中第二幅图片中的红色方框部份有待完善，明天开始继续搞爬虫，等有时间时再完善，先凑和着吧：

<a href="http://www.yanyulin.info/pages/2013/12/qqLogin_1.html">
<img src="http://www.yanyulin.info/pics/tech/qq_5.jpg"/>
</a>

<a href="http://www.yanyulin.info/pages/2013/12/qqLogin_1.html">
<img src="http://www.yanyulin.info/pics/tech/qq_6.jpg"/>
</a>

本篇博文就分析一下这个界面设计中的几个关键点，在阅读本博文之前请先阅读我<a href="http://www.yanyulin.info">个人博客</a>上关于模仿QQ界面先行篇

<a href="http://www.yanyulin.info/pages/2013/11/qqLogin.html" target="_blank">**界面编程模仿篇(模仿腾讯QQ登录界面先行篇)**</a>

本程序开源，上传至Github,下载地址：<a href="https://github.com/zwjlpeng/PQQ" target="_blank">点这里</a>

对于还不会使用github的同学，以下是我的个人博客上的两篇教程

<a href="http://www.yanyulin.info/pages/2013/11/github.html" target="_blank">**Github简明教程(入门篇)**</a>

<a href="http://www.yanyulin.info/pages/2013/11/githubM.html" target="_blank">**Github上如何给别人贡献代码**</a>

程序采用`Java`语言实现，本人只懂`C++`/`Java`/`Python`/`Shell`,其他程序语言一概不懂，等有时间再写其他两种语言的登录版本，可以订阅我的<a href="http://www.yanyulin.info">**个人博客**</a>,获取后绪相关文章与资料

1、**QQ界面登录程序最显著的地方就是界面无标题栏**，所以第一步就是去掉标题栏，Java中给`JFrame`去标题栏的方法很`easy`

	setUndecorated(true);
的确很easy是吧，但问题又出来了，是去掉了，连窗口的边框都去掉了，这肯定不是想要的结果，在这里可以采用`JInternalFrame`实现去标题栏同时保留窗口的边框，核心代码如下(代码中`jif`是`JInternalFrame`类型):

	javax.swing.plaf.InternalFrameUI jf=jif.getUI();
	((javax.swing.plaf.basic.BasicInternalFrameUI)jf).setNorthPane(null); 
	jif.setBorder(BorderFactory.createLineBorder(Color.LIGHT_GRAY, 2));

2、**QQ界面窗口居中**

	setLocation((Toolkit.getDefaultToolkit().getScreenSize().width-getSize().width)/2,
	(Toolkit.getDefaultToolkit().getScreenSize().height-getSize().height)/2);

3、由于去掉了标题栏，结果最小化，最大化，关闭均被去掉了，更重要的一个功能是窗口随鼠标拖动也被去掉了，因此这些功能都需要自已再重新实现，实现的代码也是很easy的，给JInternalFrame增加监听器，此时得注意的是监听器里操作的对象应该是JFrame,因为最终的目的是对JFrame操作，**窗口移动**的核心代码如下：
	
    //给窗体增加拖动功能
	void setWindowDray(JComponent jc){
		jc.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				isDragged=true;
				axis=new Point(e.getX(),e.getY());
				jif.setCursor(new Cursor(Cursor.MOVE_CURSOR));
			}
			@Override
			public void mouseReleased(MouseEvent e) {
				isDragged=false;
				jif.setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
			}			
		});
		jc.addMouseMotionListener(new MouseMotionAdapter() {
			@Override
			public void mouseDragged(MouseEvent e) {
				if(isDragged){
					mainLogin.setLocation(e.getXOnScreen()-axis.x,e.getYOnScreen()-axis.y);
				}
			}
		});
	}

4、**重写JPanel**，给`JPanel`增加背景图片，核心代码如下:

	URL imgUrl=getClass().getResource("pics/afternoon.jpg");
	URL textureUrl=getClass().getResource("pics/texture.png");
	ImageIcon img=new ImageIcon(imgUrl);
	ImageIcon txt=new ImageIcon(textureUrl);
	g.drawImage(img.getImage(), x, y,this.getSize().width,this.getSize().height,this);
	g.drawImage(txt.getImage(), x-50, y,this.getSize().width+100,this.getSize().height,this);

5、**按钮的相关设置**，对JButton的设置主要是设置背景的透明化，大小，内边框等，对JLabel以及JCheckbox作类似处理，相关代码例子如下：

	jbtn.setOpaque(false);
	jbtn.setMargin(new Insets(0, 0, 0, 0));
	jbtn.setContentAreaFilled(false);
	jbtn.setFocusPainted(false);  
    jbtn.setBorderPainted(false);  
    jbtn.setBorder(null);
    jbtn.addMouseListener(new ButtonListener());

6、**对JPasswordField的处理**，QQ密码限制了长度，而且禁止了copy,paste,cut,以及对文本的选择操作，在这里就要自已实现一个类继承JPasswordFiled,在这个类里面重写copy,paste,cut,同时还得重写`JPasswordField`的Document模型对像，只有重写了它，才能限制密码的输入长度，以下是限制密码长度的代码：

	public void insertString(int offs, String str, AttributeSet a)
			throws BadLocationException {
		if(this.getLength()>MAX_LENGTH)
			return ;
		else
			super.insertString(offs, str, a);
	}

7、最重要的一点，就是如何缩减代码的长度，增加代码复用，这个得自已考虑去

8、程序中不采用任何界面布局，Java中的界面布局不太适合，将布局设置成`null`,自已控制控件的位置

备注：本程序开发过程中需要用到的软件请参考
<a href="http://www.yanyulin.info/pages/2013/11/qqLogin.html" target="_blank">**界面编程模仿篇(模仿腾讯QQ登录界面先行篇)**</a>