Date: 2014-03-26
Title: WebX与Velocity是如何结合在一起的
Category: 编程语言
Tags: 淘宝技术
Slug: webx_1
Img:pics/alibaba.jpg
summary:其中Velocity就位于第三层`Turbine`,提供具体的页面驱动以及页面渲染。。Webx Turbine建立在Webx Framework的基础上，实现了页面渲染、布局、数据验证、数据提交等一系列工作。如果你单步跟踪的话，会发现`pipeline`中有一个步骤就是在执行页面的渲染。我懒得调试了，直接上代码，这是其中的一部份代码...

----------


阅读本博文时可以参考以下系列博文，WebX在前台界面上采用的是Velocity来进行渲染

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

10、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_10.html" target="_blank">Velocity中的事件初始化以及解析池初始化</a>


WebX框架的结构，如下图所示：


<a href="http://www.yanyulin.info/pages/2014/03/webx_1.html">
<img src="http://www.yanyulin.info/pics/taobao/webx1_1.jpg" alt="烟雨林博客" width="100%"/>
</a>

其中Velocity就位于第三层Turbine,提供具体的页面驱动以及页面渲染。。Webx Turbine建立在Webx Framework的基础上，实现了页面渲染、布局、数据验证、数据提交等一系列工作。如果你单步跟踪的话，会发现pipeline中有一个步骤就是在执行页面的渲染。我懒得调试了，直接上代码，这是其中的一部份代码


    protected void performScreenModule(TurbineRunData rundata) {  
         String target = assertNotNull(rundata.getTarget(), "Target was not specified");  
      
         // 从target中取得screen module名称  
         String moduleName = getModuleName(target);  
      
         // 如果设置了template，则默认打开layout  
         rundata.setLayoutEnabled(true);  
      
         try {  
    			//获取screen下面的类
             Module module = moduleLoaderService.getModuleQuiet(SCREEN_MODULE, moduleName);  
      
             // 当指定了templateName时，可以没有的screen module，而单单渲染模板。  
             // 这样就实现了page-driven，即先写模板，必要时再写一个module class与之对应。  
             if (module != null) {  
                 module.execute();  
             } else {  
                 if (isScreenModuleRequired()) {  
                     throw new ModuleNotFoundException("Could not find screen module: " + moduleName);  
                 }  
             }  
         } catch (ModuleLoaderException e) {  
             throw new WebxException("Failed to load screen module: " + moduleName, e);  
         } catch (Exception e) {  
             throw new WebxException("Failed to execute screen: " + moduleName, e);  
         }  
     } 


上面这个方法中其中最主要的就是就是看看module.execute()这个方法，跟踪这个方法的执行流程，可以看到如下方法，源代码如下:

    public void invoke(Object moduleObject, Logger log) throws Exception {  
         Object[] args = new Object[resolvers.length];  
      
         for (int i = 0; i < args.length; i++) {  
             Object value;  
      
             try {  
                 value = resolvers[i].resolve();  
             } catch (SkipModuleExecutionException e) {  
                 if (skippable) {  
                     log.debug("Module execution has been skipped. Method: {}, {}", fastMethod, e.getMessage());  
                     return;  
                 }  
      
                 value = e.getValueForNonSkippable();  
             }  
      
             // 特别处理：防止对primitive类型设置null  
             Class<?> paramType = fastMethod.getJavaMethod().getParameterTypes()[i];  
      
             if (value == null && paramType.isPrimitive()) {  
                 value = getPrimitiveDefaultValue(paramType);  
             }  
      
             args[i] = value;  
         }  
      
         try {  
             fastMethod.invoke(moduleObject, args);  
         } catch (InvocationTargetException e) {  
             throwExceptionOrError(e.getCause());  
             return;  
         }  
     }  

上面的代码大概意思就是先进行参数注解的解释，然后调用对象里的方法，具体的调用方法如下，下面这个应该是很熟悉了

    public class Hello {  
        public void execute(@Param("name") String name, Context context) {  
            context.put("name", name);  
        }  
    }  

看到context以及context.put()是不是很熟悉了，哎，我就分析到这吧，太多了，也太杂了，期待有人补充！！！