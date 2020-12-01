drawline (1, 1, maxx div 2, maxy, black)
drawline (maxx div 2, maxy, maxx, 1, black)
drawline (1, 1, maxx, 1, black)

var CheckerY, CheckerY2 : flexible array 1 .. 0 of int
var Count2 : int := 0
var Point : int
var MidPointX, MidPointY : int

var PointX := 1
var PointY := 1

var PointX2 := maxx div 2
var PointY2 := maxy

var PointX3 := maxx
var PointY3 := 1

var X, Y : int

var YY : int := (maxy) - 1
var XX : int := ((maxx div 2) + 1) - 1

var Y2 : int := 1 - maxy
var X2 : int := (maxx) - ((maxx div 2) + 1)

var EquationOfLine : int := YY div XX
var EquationOfLine2 : int := Y2 div X2



procedure Checker
    for YCheck : 1 .. round (maxy div EquationOfLine) + 1
        new CheckerY, YCheck
        CheckerY (YCheck) := maxy - (EquationOfLine * YCheck)
    end for
    for YCheck2 : 1 .. round (maxy div EquationOfLine) + 1
        new CheckerY2, YCheck2
        CheckerY2 (YCheck2) := maxy + (EquationOfLine * YCheck2)
    end for
end Checker

procedure MidPoint


end MidPoint

procedure Line
    drawfilloval (PointX, PointY, 1, 1, black)
    drawfilloval (PointX2, PointY2, 1, 1, black)
    drawfilloval (PointX3, PointY3, 1, 1, black)
    loop
        Point := Rand.Int (1, 3)
        if (Point = 1) then
            MidPointX := (X + PointX) div 2
            MidPointY := (Y + PointY) div 2
            drawfilloval (MidPointX, MidPointY, 1, 1, black)
            X := MidPointX
            Y := MidPointY
        elsif (Point = 2) then
            MidPointX := (X + 319) div 2
            MidPointY := (Y + 399) div 2
            drawfilloval (MidPointX, MidPointY, 1, 1, black)
            X := MidPointX
            Y := MidPointY
        else
            MidPointX := (X + PointX3) div 2
            MidPointY := (Y + PointY3) div 2
            drawfilloval (MidPointX, MidPointY, 1, 1, black)
            X := MidPointX
            Y := MidPointY
        end if
    end loop
end Line

procedure DrawDot
    for Count : 1 .. 255
        X := Rand.Int (215, maxx div 2 + 50)
        Y := Rand.Int (1, maxy div 2)
        if (Y > CheckerY (Count) and Y < CheckerY2 (Count)) then
            drawfilloval (X, Y, 1, 1, black)
            exit
        end if
    end for
end DrawDot

Checker
DrawDot
Line
