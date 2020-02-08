# weChatRobot 
> study link:
[wxpy包说明文档](https://wxpy.readthedocs.io/zh/latest/)
---   
## 作用
- 给特定一个好友灌鸡汤
- 回复其他好友信息（当自己忙当时候）
---   
### 依赖
> 必须先安装wxpy  
> 项目基于python3
```python
# 安装方法
pip install wxpy
# 或者
pip3 install wxpy
# 根据自己电脑的环境配置确定
```
---  
### 如果下载较慢，可以试试下面的python换阿里云源的方法
- unix/linux
    - 如果没有 .pip 或者 .pip3就创建
    - mkdir ~/.pip 或者 mkdir ~/.pip3
    - vim .pip.conf 或者 pip3.conf
    - 写入
    ```shell
    [global]
    index-url = https://mirrors.aliyun.com/pypi/simple/
    [install]
    trusted-host=mirrors.aliyun.com
    ```
- windows
    - 如果没有 C:\Users\xx\pip 或 C:\Users\xx\pip3 就创建
    - 在 C:\Users\xx\pip 或 C:\Users\xx\pip3 中创建 pip.ini 或 pip3.ini
     - 写入
    ```shell
    [global]
    index-url = https://mirrors.aliyun.com/pypi/simple/
    [install]
    trusted-host=mirrors.aliyun.com
    ```