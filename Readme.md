# 驱动级按键模拟
## 基于ctypes实现
> 更新后新增了两个scancode_down_up和keybd_event两种驱动级模拟方法,  
> 使用教程见[`VirTualKey使用说明`](https://zhuanlan.zhihu.com/p/355885881)  
> 后续将更新实际项目案例.
----------------------------------------------------------
2021.1.9更新:<br>
推荐使用keyboard和mouse模块.<br>
git上搜keyboard就行.<br>
======================================<br>
10.21日更新:

# 安装:
```
pip install VirtualKey
```
> ctypes方案对比[`pydamo`](https://github.com/bode135/pydamo "jump to the pydamo project")方案(我不知道怎么用ctypes做后台)，不支持后台模拟，但支持64位python。