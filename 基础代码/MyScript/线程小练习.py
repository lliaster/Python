# -*- coding: utf-8 -*-
# @Time     : 2024/10/28 14:11
# @Author   : Lliaster
# @File     : 线程小练习.py


"""给你一个类：

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
三个不同的线程 A、B、C 将会共用一个 Foo 实例。

线程 A 将会调用 first() 方法
线程 B 将会调用 second() 方法
线程 C 将会调用 third() 方法
请设计修改程序，以确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。

提示：

尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。
你看到的输入格式主要是为了确保测试的全面性。"""
import threading
import time


class Foo:
  def __init__(self):
    self.t = 0

  def first(self, printFirst: 'Callable[[], None]') -> None:
    printFirst()
    self.t = 1

  def second(self, printSecond: 'Callable[[], None]') -> None:
    while self.t != 1:
      pass
    printSecond()
    self.t = 2

  def third(self, printThird: 'Callable[[], None]') -> None:
    while self.t != 2:
      pass
    printThird()


if __name__=='__main__':
    foo=Foo()
    for i in range(3):
        t=Thread(target=foo)
        t.start()
