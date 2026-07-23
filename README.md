# SimpleAutoCAD

**SimpleAutoCAD** — это мощная Python-библиотека для автоматизации и программного управления Autodesk AutoCAD через COM-интерфейс.  
Она предоставляет интуитивно понятный объектно-ориентированный интерфейс к объектной модели AutoCAD, позволяя создавать, редактировать и управлять 2D‑ и 3D‑чертежами непосредственно из Python-скриптов.

---

## Содержание

- [SimpleAutoCAD](#simpleautocad)
  - [Содержание](#содержание)
  - [Особенности](#особенности)
  - [Установка](#установка)
  - [Быстрый старт](#быстрый-старт)
  - [Основные компоненты](#основные-компоненты)
      - [AutoCAD – главный класс](#autocad--главный-класс)
      - [PyGe – геометрические примитивы](#pyge--геометрические-примитивы)
      - [Работа с XData](#работа-с-xdata)
  - [Примеры](#примеры)
      - [Создание отрезка](#создание-отрезка)
      - [Аналоговые часы](#аналоговые-часы)
      - [Запись и чтение XData](#запись-и-чтение-xdata)
      - [Работа с блоками и атрибутами](#работа-с-блоками-и-атрибутами)
      - [Геометрические преобразования](#геометрические-преобразования)
  - [Автор](#автор)
  - [☕ Поддержать проект](#-поддержать-проект)

---

## <a name="features"></a>Особенности

- **Полный контроль над AutoCAD** – использует объектную модель ActiveX/COM для взаимодействия с установленным приложением AutoCAD, позволяя автоматизировать практически любую задачу.
- **Продвинутая работа с геометрией** – включает набор классов `PyGe` для выполнения сложных геометрических вычислений, функционально аналогичных нативным классам `AcGe` из ObjectARX.
- **Автоматизация рутинных задач** – создание слоёв, блоков, примитивов, атрибутов, работа с XData, таблицами, печатью и т.д.
- **Простота интеграции** – разрабатывайте собственные приложения на Python без глубокого погружения в C++ или AutoLISP.
- **Кроссплатформенность** – работает на любой системе Windows с установленным AutoCAD (2000 и новее).

---

## <a name="installation"></a>Установка

```bash
pip install simpleautocad
```
```bash
pip install git+https://github.com/busy4beaver/simpleautocad.git
```

Системные требования:

    ОС: Windows (7, 8, 10, 11)

    Установленный AutoCAD (версия 2000 или выше)

    Python 3.8 и выше

## <a name="quick-start"></a>Быстрый старт

Подключение к AutoCAD, создание линии в пространстве модели с настройкой цвета, типа линии и веса.

```python
from simpleautocad import AutoCAD, PyGePoint3d, AcLineWeight, AcRegenType

def create_line():
    # Подключаемся к AutoCAD
    acad = AutoCAD()
    # Делаем окно видимым
    acad.Visible = True
    # Активный документ
    doc = acad.ActiveDocument
    # Пространство модели
    model_space = doc.ModelSpace

    # Создаём начальную и конечную точку для отрезка
    start_pt = PyGePoint3d()          # x=0, y=0, z=0
    end_pt = PyGePoint3d(10, 10)      # x=10, y=10, z=0

    # Добавляем линию
    line = model_space.AddLine(start_pt, end_pt)

    # Получаем интерфейс AcCmColor для установки цвета
    color = acad.uGetAcadAcCmColor()
    # Устанавливаем RGB цвет
    color.SetRGB(10, 110, 210)
    # Применяем цвет к отрезку
    line.TrueColor = color
    # Применяем тип линии
    line.Linetype = 'DASHED'
    # Применяем вес линий
    line.Lineweight = AcLineWeight.acLnWt020
    # Обновляем экран
    doc.Regen(AcRegenType.acAllViewports)

if __name__ == "__main__":
    create_line()
```

## <a name="components"></a>Основные компоненты
#### AutoCAD – главный класс

Наследуется от AcadApplication и предоставляет дополнительные удобные методы:

    uGetAcadAcCmColor() – создаёт объект цвета.

    uGetAcadLayerStateManager() – менеджер состояний слоёв.

    uSetXData(obj, xdm) – записывает расширенные данные.

    uGetObjectType(obj) – возвращает Python-тип объекта (например, AcadCircle).

```python
from simpleautocad import AutoCAD

app = AutoCAD()
app.Visible = True
doc = app.ActiveDocument
ms = doc.ModelSpace
```

#### PyGe – геометрические примитивы

Набор классов для работы с геометрией:

    PyGePoint3d / PyGePoint2d – точки (3D и 2D)

    PyGeVector3d / PyGeVector2d – векторы

    PyGeMatrix3d / PyGeMatrix2d – матрицы преобразований (поворот, перенос, масштабирование, отражение, проекция)

Поддерживаются арифметические операции, нормализация, скалярное и векторное произведения, углы и т.д.

```python
from simpleautocad import PyGePoint3d, PyGeVector3d, PyGeMatrix3d

p1 = PyGePoint3d(1, 2, 3)
v = PyGeVector3d(1, 1, 1)
p2 = p1 + v           # точка + вектор
dist = p1.distanceTo(p2)
```

#### Работа с XData

XDataManager и DxfGroupXDCode позволяют удобно записывать и читать расширенные данные (пример ниже).

## <a name="examples"></a>Примеры

#### Создание отрезка

Базовые операции: создание линии, установка цвета, типа линии и веса, а также регенерация чертежа.

```python
from simpleautocad import AutoCAD, PyGePoint3d, AcLineWeight, AcRegenType

def create_line():
    # Подключаемся к AutoCAD
    acad = AutoCAD()
    # Делаем окно видимым
    acad.Visible = True
    # Активный документ
    doc = acad.ActiveDocument
    # Пространство модели
    model_space = doc.ModelSpace

    # Создаём начальную и конечную точку для отрезка
    start_pt = PyGePoint3d()          # x=0, y=0, z=0
    end_pt = PyGePoint3d(10, 10)      # x=10, y=10, z=0

    # Добавляем линию
    line = model_space.AddLine(start_pt, end_pt)

    # Получаем интерфейс AcCmColor для установки цвета
    color = acad.uGetAcadAcCmColor()
    # Устанавливаем RGB цвет
    color.SetRGB(10, 110, 210)
    # Применяем цвет к отрезку
    line.TrueColor = color
    # Применяем тип линии
    line.Linetype = 'DASHED'
    # Применяем вес линий
    line.Lineweight = AcLineWeight.acLnWt020
    # Обновляем экран
    doc.Regen(AcRegenType.acAllViewports)

if __name__ == "__main__":
    create_line()
```

#### Аналоговые часы

Этот пример показывает, как создать циферблат, текстовые метки, стрелки и анимировать их в реальном времени с помощью бесконечного цикла. Также демонстрируется использование массивов (ArrayPolar) и матриц поворота.

```python
from simpleautocad import AutoCAD, AcadLine, AcadMtext, PyGePoint3d, PyGeVector3d, PyGeMatrix3d, AcLineWeight, AcAttachmentPoint, AcRegenType, AcColor, vInteger
import math
import time
from datetime import datetime
from zoneinfo import ZoneInfo

def test_clock():
    # Подключаемся к AutoCAD
    app = AutoCAD()
    app.Visible = True
    doc = app.ActiveDocument
    ms = doc.ModelSpace

    # Центр и размер
    center = PyGePoint3d()
    size = 10
    icolor = app.uGetAcadAcCmColor()
    ang_1_60 = -math.radians(6)  # поворот на 6° по часовой

    # Отрисовка шкалы
    pt1 = PyGePoint3d(center.x, center.y + size - size/10)
    pt2 = PyGePoint3d(center.x, center.y + size)
    line = ms.AddLine(pt1, pt2)
    hinspt = PyGePoint3d(pt1.x, pt1.y - size/6)

    icolor.ColorIndex = 251
    line.TrueColor = icolor
    lines = line.ArrayPolar(60, -math.pi*2 - ang_1_60, center)
    line.ScaleEntity(line.EndPoint, 1.5)
    line.Lineweight = AcLineWeight.acLnWt050
    icolor.ColorIndex = AcColor.acMagenta
    line.TrueColor = icolor
    for i in range(4, 59, 5):
        objLine = AcadLine(lines[i])
        objLine.ScaleEntity(objLine.EndPoint, 1.5)
        objLine.Lineweight = AcLineWeight.acLnWt050
        objLine.TrueColor = icolor

    # Текстовые метки (12 часов)
    hour_txt = ms.AddMText(hinspt, size/6, '12')
    hour_txt.Height = size/8
    hour_txt.AttachmentPoint = AcAttachmentPoint.acAttachmentPointMiddleCenter
    hour_txt.InsertionPoint = hinspt
    icolor.ColorIndex = 250
    hour_txt.TrueColor = icolor

    hours = hour_txt.ArrayPolar(12, -math.pi*2 - ang_1_60*5, center)
    for i in range(0, 11):
        objHour = AcadMtext(hours[i])
        objHour.TextString = str(i+1)
        objHour.Rotate(objHour.InsertionPoint, -ang_1_60*5*(i+1))

    # Стрелки (секундная, минутная, часовая)
    line_sec = ms.AddLine(PyGePoint3d(center.x, center.y - size/6), PyGePoint3d(center.x, center.y + size - size/10 - size/40))
    icolor.SetRGB(255, 0, 0)
    line_sec.TrueColor = icolor
    line_sec.Lineweight = AcLineWeight.acLnWt030

    line_min = ms.AddLine(PyGePoint3d(center.x, center.y - size/6), PyGePoint3d(center.x, center.y + size - size/10 - size/8))
    icolor.SetRGB(0, 255, 0)
    line_min.TrueColor = icolor
    line_min.Lineweight = AcLineWeight.acLnWt030

    line_hour = ms.AddLine(PyGePoint3d(center.x, center.y - size/6), PyGePoint3d(center.x, center.y + size - size/10 - size/4))
    icolor.SetRGB(0, 0, 255)
    line_hour.TrueColor = icolor
    line_hour.Lineweight = AcLineWeight.acLnWt030

    # Включаем отображение веса линий
    if not doc.GetVariable('LWDISPLAY'):
        doc.SetVariable('LWDISPLAY', vInteger(1))

    # Матрицы поворота для 60 положений
    rotation_matrixes = []
    for i in range(0, 60):
        mat = PyGeMatrix3d.rotation(ang_1_60 * i, PyGeVector3d.kZaxis, center)
        rotation_matrixes.append(mat)

    # Текущее время
    mytime = datetime.now(ZoneInfo("Asia/Novosibirsk"))
    my_h, my_m, my_s = mytime.hour, mytime.minute, mytime.second

    # Поворот стрелок
    line_sec.TransformBy(rotation_matrixes[my_s])
    line_min.TransformBy(rotation_matrixes[my_m])
    idx = (my_h if my_h < 12 else my_h - 12) * 5 + (my_m // 12)
    line_hour.TransformBy(rotation_matrixes[idx])

    # Вид
    viewport = doc.ActiveViewport
    viewport.Direction = PyGeVector3d(-1, -1, 1)
    doc.ActiveViewport = viewport
    app.ZoomAll()

    # Бесконечный цикл обновления стрелок
    while True:
        mytime = datetime.now(ZoneInfo("Asia/Novosibirsk"))
        regen = False
        if my_s != mytime.second:
            idx = abs(mytime.second - my_s)
            if idx == 59 and mytime.second == 0: idx = 1
            line_sec.TransformBy(rotation_matrixes[idx])
            my_s = mytime.second
            regen = True
        if my_m != mytime.minute:
            idx = abs(mytime.minute - my_m)
            if idx == 59 and mytime.minute == 0: idx = 1
            line_min.TransformBy(rotation_matrixes[idx])
            my_m = mytime.minute
            if not (my_m % 12):
                line_hour.TransformBy(rotation_matrixes[1])
            regen = True
        if regen:
            doc.Regen(AcRegenType.acActiveViewport)
            print(f"{my_h:02}:{my_m:02}:{my_s:02}")
        time.sleep(0.2)
```

#### Запись и чтение XData

Пример демонстрирует, как добавлять зарегистрированное приложение, записывать XData в объекты (окружности), а затем считывать и применять эту информацию для создания штриховки нужного цвета.

```python
from simpleautocad import *

def test_xdata():
    app = AutoCAD()
    app.Visible = True
    doc = app.ActiveDocument
    ms = doc.ModelSpace

    radius = 4
    regAppName = 'AppCircleColor'
    icolor = app.uGetAcadAcCmColor()

    pt1 = PyGePoint3d(10, 30)
    pt2 = PyGePoint3d(10, 20)
    pt3 = PyGePoint3d(10, 10)

    cir1 = ms.AddCircle(pt1, radius)
    cir2 = ms.AddCircle(pt2, radius)
    cir3 = ms.AddCircle(pt3, radius)

    # Подготовка данных
    xdm1 = XDataManager(regAppName)
    xdm1.add_data(DxfGroupXDCode.kDxfXdInteger16, AcColor.acRed)

    xdm2 = XDataManager(regAppName)
    xdm2.add_data(DxfGroupXDCode.kDxfXdInteger16, AcColor.acYellow)

    xdm3 = XDataManager(regAppName)
    xdm3.add_data(DxfGroupXDCode.kDxfXdInteger16, AcColor.acGreen)

    # Запись
    app.uSetXData(cir1, xdm1)
    app.uSetXData(cir2, xdm2)
    app.uSetXData(cir3, xdm3)

    # Чтение и применение штриховки
    for obj in ms:
        if app.uGetObjectType(obj) is AcadCircle:
            xdata = obj.GetXData(regAppName)
            if xdata[0]:
                if xdata[0][1] == DxfGroupXDCode.kDxfXdInteger16:
                    icolor.ColorIndex = xdata[1][1]
                else:
                    icolor.ColorIndex = 255
                hatch = ms.AddHatch(AcPatternType.acHatchPatternTypePreDefined, 'SOLID', True, AcHatchObjectType.acHatchObject)
                hatch.TrueColor = icolor
                hatch.AppendInnerLoop(vObjectArray(obj))
    doc.Regen(AcRegenType.acActiveViewport)
```

#### Работа с блоками и атрибутами

Класс BlockReference позволяет удобно работать с блоками, имеющими атрибуты и динамические свойства. Пример для пользовательского блока:

```python
from simpleautocad import BlockReference, AutoCAD, PyGePoint3d

class MyBlock(BlockReference):
    BlockName = "MY_BLOCK"  # Имя блока в чертеже

    @property
    def my_attribute(self):
        return self.get_attribute_value("ATTR1")

    @my_attribute.setter
    def my_attribute(self, value):
        self.set_attribute_value("ATTR1", value)

# Использование
app = AutoCAD()
ms = app.ActiveDocument.ModelSpace

# Вставка блока
block = MyBlock()
block.insert(PyGePoint3d(0, 0, 0), ms)
block.my_attribute = "Новое значение"
```

#### Геометрические преобразования

Использование матрицы для поворота объектов относительно произвольной точки:

```python
from simpleautocad import AutoCAD, PyGePoint3d, PyGeVector3d, PyGeMatrix3d

app = AutoCAD()
ms = app.ActiveDocument.ModelSpace

# Создаём линию
line = ms.AddLine(PyGePoint3d(0, 0, 0), PyGePoint3d(10, 0, 0))

# Поворачиваем на 45° вокруг точки (5, 0, 0)
center = PyGePoint3d(5, 0, 0)
axis = PyGeVector3d.kZaxis   # ось Z
angle = math.radians(45)
matrix = PyGeMatrix3d.rotation(angle, axis, center)
line.TransformBy(matrix)

# Масштабируем в 2 раза относительно центра
matrix_scale = PyGeMatrix3d.scaling(2.0, center)
line.TransformBy(matrix_scale)
```

## <a name="author"></a>Автор

 - [Андрей Литвинов](https://t.me/busy4beaver)
  
## ☕ Поддержать проект

Если этот проект оказался вам полезен, вы можете поддержать его развитие:

[![YooMoney](https://img.shields.io/badge/Donation-Yoo.money-blue.svg)](https://yoomoney.ru/to/4100118099549894) 
[![Boosty](https://img.shields.io/badge/Boosty-donate-orange.svg)](https://boosty.to/busybeaver/donate)
