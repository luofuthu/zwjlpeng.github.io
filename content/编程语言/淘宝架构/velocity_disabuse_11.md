Date: 2014-03-27
Title: Velocity中对宏的初始化过程分析
Category: 编程语言
Tags: 淘宝技术
Slug: velocity_disabuse_11
Img:pics/company/taobao.jpg
summary:当`Velocity`运行时，会载入一个全局的宏文件。所有模板都可访问该宏文件，这个文件位置在相对于资源文件的根目录下，此外，还有一些其他配置来处理宏的不同使用情况，例如，定义在模板中是否可用#macro()指令定义一个新的宏。默认为true，表示所有的vm都可以新建宏，但是要注意可能会把全局的宏...

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

10、<a href="http://www.yanyulin.info/pages/2014/03/velocity_disabuse_10.html" target="_blank">Velocity中的事件初始化以及解析池初始化</a>

当Velocity engine运行时，会载入一个全局的宏文件。所有模板都可访问该宏文件(Velocimacros). 这个文件位置在相对于资源文件的根目录下。velocity默认的配置项为


    velocimacro.library = VM_global_library.vm
　　

此外，还有一些其他配置来处理宏的不同使用情况，例如：
　　

    velocimacro.permissions.allow.inline = true

定义在模板中是否可用#macro()指令定义一个新的宏。默认为true，表示所有的vm都可以新建宏，但是要注意可能会把全局的宏配置给替换掉。
　　


    velocimacro.permissions.allow.inline.to.replace.global = false

控制用户定义的宏是否可以可以替换Velocity的全局宏。



    velocimacro.library.autoreload = false

控制宏是否自动载入。当值为true时宏将根据是否修改而决定是否需要重新加载，这个特性可在调试时很方便，不需重启你的服务器。
	

还是让我们来看看源代码吧，文字不如代码来的直接，下面这个看似很长的代码，其实在我们的例子中用到的不是很多，因为我们的例子中默认配置文件中没有配置项


    velocimacro.library = VM_global_library.vm

目录下也没有`VM_global_library.vm`这个文件

    public void initVelocimacro()  
     {  
         /* 
          *  maybe I'm just paranoid... 
          */  
         synchronized(this)  
         {  
    		//日志信息打印
             log.trace("initialization starting.");  
      
             /* 
              *   allow replacements while we add the libraries, if exist 
              */  
    			//允许宏进行替换，即局部可以替换全局
             setReplacementPermission(true);  
      
             /* 
              *  add all library macros to the global namespace 
              */  
      //命令空间的设定
             vmManager.setNamespaceUsage(false);  
      
             /* 
              *  now, if there is a global or local libraries specified, use them. 
              *  All we have to do is get the template. The template will be parsed; 
              *  VM's  are added during the parse phase 
              */  
      		//下面这个由于默认配置没有这个配置项，因此libfiles=null
              Object libfiles = rsvc.getProperty(RuntimeConstants.VM_LIBRARY);  
      
              if (libfiles == null)  
              {    //日志打印
                  log.debug("\"" + RuntimeConstants.VM_LIBRARY +  
                      "\" is not set.  Trying default library: " +  
                      RuntimeConstants.VM_LIBRARY_DEFAULT);  
      
                  // try the default library.  
    				//去我们目录下寻找全局宏文件VM_global_library.vm，目录下没有这个					//文件,因些函数调用的结果很显然是null
                  if (rsvc.getLoaderNameForResource(RuntimeConstants.VM_LIBRARY_DEFAULT) != null)  
                  {  
                      libfiles = RuntimeConstants.VM_LIBRARY_DEFAULT;  
                  }  
                  else  
                  {   //日志打印
                      log.debug("Default library not found.");  
                  }  
              }  
      		//对于我们的程序来说，由于采用默认配置，配置中少了配置项，因此					//libfile=null,下面一段均不执行
              if(libfiles != null)  
              {  //如果有配置文件的话，将会对其进行分析
                  macroLibVec = new ArrayList();  
                  if (libfiles instanceof Vector)  
                  {  
                      macroLibVec.addAll((Vector)libfiles);  
                  }  
                  else if (libfiles instanceof String)  
                  {  
                      macroLibVec.add(libfiles);  
                  }  
      
                  for(int i = 0, is = macroLibVec.size(); i < is; i++)  
                  {  
                      String lib = (String) macroLibVec.get(i);  
      
                      /* 
                       * only if it's a non-empty string do we bother 
                       */  
      
                      if (StringUtils.isNotEmpty(lib))  
                      {  
                          /* 
                           *  let the VMManager know that the following is coming 
                           *  from libraries - need to know for auto-load 
                           */  
      
                          vmManager.setRegisterFromLib(true);  
      
                          log.debug("adding VMs from VM library : " + lib);  
      
                          try  
                          {  
                              Template template = rsvc.getTemplate(lib);  
      
                              /* 
                               *  save the template.  This depends on the assumption 
                               *  that the Template object won't change - currently 
                               *  this is how the Resource manager works 
                               */  
      
                              Twonk twonk = new Twonk();  
                              twonk.template = template;  
                              twonk.modificationTime = template.getLastModified();  
                              libModMap.put(lib, twonk);  
                          }  
                          catch (Exception e)  
                          {  
                              String msg = "Velocimacro : Error using VM library : " + lib;  
                              log.error(true, msg, e);  
                              throw new VelocityException(msg, e);  
                          }  
      
                          log.trace("VM library registration complete.");  
      
                          vmManager.setRegisterFromLib(false);  
                      }  
                  }  
              }  
      
             /* 
              *   now, the permissions 
              */  
      
      
             /* 
              *  allowinline : anything after this will be an inline macro, I think 
              *  there is the question if a #include is an inline, and I think so 
              * 
              *  default = true 
              */  
      //允许填加宏
             setAddMacroPermission(true);  
      		//判断是否允许宏的递归
             if (!rsvc.getBoolean( RuntimeConstants.VM_PERM_ALLOW_INLINE, true))  
             {  
                 setAddMacroPermission(false);  
      
                 log.debug("allowInline = false : VMs can NOT be defined inline in templates");  
             }  
             else  
             {  
                 log.debug("allowInline = true : VMs can be defined inline in templates");  
             }  
      
             /* 
              *  allowInlineToReplaceGlobal : allows an inline VM , if allowed at all, 
              *  to replace an existing global VM 
              * 
              *  default = false 
              */  
             setReplacementPermission(false);  
      
             if (rsvc.getBoolean(  
                  RuntimeConstants.VM_PERM_ALLOW_INLINE_REPLACE_GLOBAL, false))  
             {  
                 setReplacementPermission(true);  
                   
                 log.debug("allowInlineToOverride = true : VMs " +  
                     "defined inline may replace previous VM definitions");  
             }  
             else  
             {  
                 log.debug("allowInlineToOverride = false : VMs " +  
                     "defined inline may NOT replace previous VM definitions");  
             }  
      
             /* 
              * now turn on namespace handling as far as permissions allow in the 
              * manager, and also set it here for gating purposes 
              */  
             vmManager.setNamespaceUsage(true);  
      
             /* 
              *  template-local inline VM mode : default is off 
              */  
             setTemplateLocalInline(rsvc.getBoolean(  
                 RuntimeConstants.VM_PERM_INLINE_LOCAL, false));  
      
             if (getTemplateLocalInline())  
             {  
                 log.debug("allowInlineLocal = true : VMs " +  
                     "defined inline will be local to their defining template only.");  
             }  
             else  
             {  
                 log.debug("allowInlineLocal = false : VMs " +  
                     "defined inline will be global in scope if allowed.");  
             }  
      
             vmManager.setTemplateLocalInlineVM(getTemplateLocalInline());  
      
             /* 
              *  autoload VM libraries 
              */  
             setAutoload(rsvc.getBoolean(RuntimeConstants.VM_LIBRARY_AUTORELOAD, false));  
      
             if (getAutoload())  
             {  
                 log.debug("autoload on : VM system " +  
                      "will automatically reload global library macros");  
             }  
             else  
             {  
                 log.debug("autoload off : VM system " +  
                       "will not automatically reload global library macros");  
             }  
      
             log.trace("Velocimacro : initialization complete.");  
         }  
     }  

