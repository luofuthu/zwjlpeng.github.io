Date: 2014-03-16
Title: Velocity入门例子自定义呈现容器
Category: 编程语言
Tags: 淘宝技术
Slug: velocity_disabuse_2
Img:pics/company/taobao.jpg
summary:本篇博文仅随前一篇博文而来<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_1.html" target="_blank">Velocity入门教程HelloWord程序</a>本篇博文主要介绍Velocity中如何自定义呈现容器即，例子中实现的是自定义义的VelocityContext容器，用自定义的容器来渲染模板文件，并将结果输出，自定义的呈现容器使用HashMap来存放键值对,从代码中可以看出自定义呈现容器中只能向...

----------

本篇博文仅随前一篇博文而来

<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_1.html" target="_blank">
Velocity入门教程HelloWord程序
</a>

本篇博文主要介绍velocity中如何自定义呈现容器即`VelocityContext`

例子中实现的是自定义义的VelocityContext容器，用自定义的容器来渲染模板文件，并将结果输出

	//自定义的VelocityContext  
	class DBContext extends AbstractContext{  
	    private Map<String,Object> props=new HashMap<String, Object>();  
	    public void setUp(){  
	    }  
	    public DBContext(){  
	        super();  
	    }  
	    public DBContext(Context inner){  
	        super(inner);  
	    }  
	    @Override  
	    public boolean internalContainsKey(Object arg0) {  
	        return false;  
	    }  
	    @Override  
	    public Object internalGet(String arg0) {  
	        Object pp=props.get(arg0);  
	        return pp;  
	    }  
	    @Override  
	    public Object[] internalGetKeys() {  
	        return null;  
	    }  
	    @Override  
	    public Object internalPut(String key, Object value) {  
	        props.put(key, value);  
	        return null;  
	    }  
	    @Override  
	    public Object internalRemove(Object arg0) {  
	        return null;  
	    }  
	}  
	public class DBContextTest {  
	    public DBContextTest(String templateFile){  
	        //初始化Velocity模板引擎，为单例模式  
	        RuntimeSingleton.init(new Properties());  
	        //获取模板文件  
	        Template template=RuntimeSingleton.getTemplate(templateFile);  
	        //创建一个VelocityContext对象，这里使用的是自定义的VelocityContext对象  
	        DBContext dbc=new DBContext();  
	        //创建一个Hashtable对象  
	        Hashtable<String, String> h=new Hashtable<String,String>();  
	        //向创建的Hashtable对象里填加值  
	        h.put("Bar", "来自于hashtable");  
	        //向VelocityContext容器中填加两个值  
	        dbc.put("string", "欢迎");  
	        dbc.put("hashtable", h);  
	        Writer writer=new BufferedWriter(new OutputStreamWriter(System.out));  
	        //使用自定义的VelocityContext对template进行渲染，并将渲染的结果输出到writer中  
	        template.merge(dbc, writer);  
	        try {  
	        //清空缓存，防止因缓存而打印不全  
	            writer.flush();  
	            writer.close();  
	        } catch (Exception e) {  
	            System.out.println(e.getMessage());  
	        }  
	    }  
	    public static void main(String[] args) {  
	        DBContextTest t;  
	        t=new DBContextTest("test2.vm");  
	    }  
	}  

**备注**

1、自定义的呈现容器使用HashMap来存放键值对

2、从代码中可以看出自定义呈现容器中只能向HaspMap中增加元素，而无法从容器中删除元素


3、从主程序代码中可以看出Velocity模板引擎实例化为单例模式，什么叫单例模式可以参考设计模式一书


后台的模板文件如下如示，即函数的参数`templateFile`

    ##Hello 来自于 $name 在 $project 工程里.  
    $string  
    ##实际上调用 的是hashtable.get("Bar")  
    $hashtable.Bar  
    ##将值全部打印出来  
    #foreach($value in $hashtable.keySet())  
    $hashtable.get($value)  
    #end  

