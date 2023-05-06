# Lagrange-interpolation
该程序使用Python编写，使用三点拉格朗日插值法计算函数的插值。最初采用3个点进行插值时误差较大。即使缩小采样区间，仍会导致过程十分繁琐。因此，进行了改进：如果设置1000个采样点，则可以通过先判断被插值点在采样点中的位置，再取靠近的三个点进行三点插值，从而避免上述的误差和繁琐的过程，并得到很好的拟合结果。代码中有详细注释，以便您更好地理解其内容。

The program is written in Python and uses the three-point Lagrange interpolation method to calculate the interpolation of the function. Initially, using only three points for interpolation resulted in a large error. Even if the sampling interval is reduced, it still leads to a cumbersome process. Therefore, improvements have been made: if 1000 sampling points are set, the program can first determine the position of the interpolated point among the sampling points, and then take the nearest three points for three-point interpolation, thus avoiding the aforementioned errors and tedious process, and obtaining good fitting results. The code has detailed comments to help you better understand its content.
