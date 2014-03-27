Date: 2014-03-26
Title: Velocity中的事件初始化以及解析池初始化
Category: 编程语言
Tags: 淘宝技术
Slug: velocity_disabuse_10
Img:pics/company/taobao.jpg
summary:同样代码也是非常多的，直接列出代码，以注释的方式进行解释，可以结合<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_3.html" target="_blank">Velocity入门例子事件监听机制</a>分析一下，<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_3.html" target="_blank">Velocity入门例子事件监听机制</a>就是对给引擎填加了事件处理机制,好了，又到了一个比较关键的部份了，解析池的初始化，直接源码吧，少写文字，上面的代码，我觉的最重要的还有一个函数，`createNewParser()`,这个函数就不分析了...

----------

**本系列教程，为个人在淘宝实习所写，博文中所提及的WebX为淘宝的架构，大家可以忽略，当然有兴趣的，也可以自已去搜搜，淘宝的WebX目前处于开源状态**

**Velocity引擎解惑**

1、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_1.html" target="_blank">Velocity入门教程HelloWord程序</a>

2、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_2.html" target="_blank">Velocity入门例子自定义呈现容器</a>

3、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_3.html" target="_blank">Velocity入门例子事件监听机制</a>


4、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_4.html" target="_blank">Velocity入门例子创建普通的web工程</a>

5、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_5.html" target="_blank">Velocity中的单例模式以及多实例模式</a>

6、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_6.html" target="_blank">velocity初始化过程分析读取配置文件</a>

7、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_7.html" target="_blank">velocity初始化日志系统的过程分析</a>

8、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_8.html" target="_blank">Velocity初始化资源加载器以及预指令</a>

9、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_9.html" target="_blank">Velocity语法简明教程</a>

同样代码也是非常多的，直接列出代码，以注释的方式进行解释，可以结合<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_3.html" target="_blank">Velocity入门例子事件监听机制</a>分析一下，<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_3.html" target="_blank">Velocity入门例子事件监听机制</a>就是对给引擎填加了事件处理机制

    private void initializeEventHandlers()  
      {  
      /*
      eventCartridge是一个事件筒，里面装有各种各样的事件，如果查看其源代码实现可以			发现如下：
      private List referenceHandlers = new ArrayList();
      private List nullSetHandlers = new ArrayList();
      private List methodExceptionHandlers = new ArrayList();
      private List includeHandlers = new ArrayList();
      private List invalidReferenceHandlers = new ArrayList();
      从上面可以看出Velocity在渲染页面的时候，提供了不同的EventHandler，供开发者调用
     */
      eventCartridge = new EventCartridge();  
  
      /** 
       * For each type of event handler, get the class name, instantiate it, and store it. 
      */  
       /*
    	 看到下面这行代码，是不是已经很熟悉了，同样是读取配置文件，从配置文件中获取
         能够解析引用插入的事件处理类，默认配置文件中并没有进行配置
       */
       String[] referenceinsertion = configuration.getStringArray(RuntimeConstants.EVENTHANDLER_REFERENCEINSERTION);  
       if ( referenceinsertion != null )  
         {  //由于默认配置文件没有配置，因此下面的代码未执行
             for ( int i=0; i < referenceinsertion.length; i++ )  
              {  //如果配置了话就会实例化一个特定的该类的处理器
                  EventHandler ev = initializeSpecificEventHandler(referenceinsertion[i],RuntimeConstants.EVENTHANDLER_REFERENCEINSERTION,ReferenceInsertionEventHandler.class);  
                  if (ev != null)  //如果不为空的话，将其加入事件处理筒里面
                      eventCartridge.addReferenceInsertionEventHandler((ReferenceInsertionEventHandler) ev);  
              }  
          }  
      //当使用#set()语法时，设置一个NULL值的时候，就会触发此事件
          String[] nullset = configuration.getStringArray(RuntimeConstants.EVENTHANDLER_NULLSET);  
          if ( nullset != null )  
          {  
              for ( int i=0; i < nullset.length; i++ )  
              {  
                  EventHandler ev = initializeSpecificEventHandler(nullset[i],RuntimeConstants.EVENTHANDLER_NULLSET,NullSetEventHandler.class);  
                  if (ev != null)  
                      eventCartridge.addNullSetEventHandler((NullSetEventHandler) ev);  
              }  
          }  
      //渲染模板，一旦发现调用的方法抛出异常，就会触发该事件，允许开发事处理这个异常， 
      //输出更加友好的信息
          String[] methodexception = configuration.getStringArray(RuntimeConstants.EVENTHANDLER_METHODEXCEPTION);  
          if ( methodexception != null )  
          {  
              for ( int i=0; i < methodexception.length; i++ )  
              {  
                  EventHandler ev = initializeSpecificEventHandler(methodexception[i],RuntimeConstants.EVENTHANDLER_METHODEXCEPTION,MethodExceptionEventHandler.class);  
                  if (ev != null)  
                      eventCartridge.addMethodExceptionHandler((MethodExceptionEventHandler) ev);  
              }  
          }  
       //处理#include与#parse的时候的事件处理机制
          String[] includeHandler = configuration.getStringArray(RuntimeConstants.EVENTHANDLER_INCLUDE);  
          if ( includeHandler != null )  
          {  
              for ( int i=0; i < includeHandler.length; i++ )  
              {  
                  EventHandler ev = initializeSpecificEventHandler(includeHandler[i],RuntimeConstants.EVENTHANDLER_INCLUDE,IncludeEventHandler.class);  
                  if (ev != null)  
                      eventCartridge.addIncludeEventHandler((IncludeEventHandler) ev);  
              }  
          }  
      	 //渲染页面时，遇到非法引用时会产生该异常
          String[] invalidReferenceSet = configuration.getStringArray(RuntimeConstants.EVENTHANDLER_INVALIDREFERENCES);  
          if ( invalidReferenceSet != null )  
          {  
              for ( int i=0; i < invalidReferenceSet.length; i++ )  
              {  
                  EventHandler ev = initializeSpecificEventHandler(invalidReferenceSet[i],RuntimeConstants.EVENTHANDLER_INVALIDREFERENCES,InvalidReferenceEventHandler.class);  
                  if (ev != null)  
                  {  
                      eventCartridge.addInvalidReferenceEventHandler((InvalidReferenceEventHandler) ev);  
                  }  
              }  
          }  
      } 

**initializeParserPool(初始化解析池)**

好了，又到了一个比较关键的部份了，解析池的初始化，直接源码吧，少写文字

    private void initializeParserPool()  
    {  
    /* 
     * Which parser pool? 
     */  
    //上面已经多次出现这个方法，获取解析池的类名，即配置文件中配置的
    // org.apache.velocity.runtime.ParserPoolImpl（类名）
    String pp = getString(RuntimeConstants.PARSER_POOL_CLASS);  
    //判断pp是否成功赋值，如果成功赋值了就执行下面的逻辑，默认配置文件中显示有这个		   //配置，因此pp肯定不为NULL,下面逻辑必然执行
    	if (pp != null && pp.length() > 0)  
        {  
            /* 
             *  if something was specified, then make one. 
             *  if that isn't a ParserPool, consider 
             *  this a huge error and throw 
             */  
      
            Object o = null;  
      
            try  
            {  //根据类名来实例化类，这是Java的反射机制的运用的一个典型，不多讲
                o = ClassUtils.getNewInstance( pp );  
            }  
            catch (ClassNotFoundException cnfe )  
            {  
                String err = "The specified class for ParserPool ("  
                    + pp  
                    + ") does not exist (or is not accessible to the current classloader.";  
                log.error(err);  
                throw new VelocityException(err, cnfe);  
            }  
            catch (InstantiationException ie)  
            {  
              throw new VelocityException("Could not instantiate class '" + pp + "'", ie);  
            }  
            catch (IllegalAccessException ae)  
            {  
              throw new VelocityException("Cannot access class '" + pp + "'", ae);  
            }  
      	   //如果o未实现解析池的接口，则出错返回
            if (!(o instanceof ParserPool))  
            {  
                String err = "The specified class for ParserPool ("  
                    + pp + ") does not implement " + ParserPool.class  
                    + " Velocity not initialized correctly.";  
      
                log.error(err);  
                throw new VelocityException(err);  
            }  
         //将解析池的实例引用保存在类的私有变量中
            parserPool = (ParserPool) o;  
         //解析池的初始化
            parserPool.initialize(this);  
        }  
        //如果配置文件中没有指定解析池，则会出错
        else  
        {  
        /* 
         *  someone screwed up.  Lets not fool around... 
         */  
           String err = "It appears that no class was specified as the"  
                + " ParserPool.  Please ensure that all configuration"  
                + " information is correct.";  
      
           log.error(err);  
           throw new VelocityException( err );  
        }  
    } 

上面的代码，我觉的最重要的还有一个函数，createNewParser(),这个函数就不分析了。

