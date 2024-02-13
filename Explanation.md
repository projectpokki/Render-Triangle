On a 2d plane, the position of a point $P$ relative to a triangle $\Delta ABC$ can be represented by 3 vectors:
- $A$, a vertex of $\Delta ABC$
- $v_B$, a vector parallel to $\overline{AB}$
- $v_C$ is a vector parallel to $\overline{AC}$

Using these vectors, the position of $P$ can be represented as:
$$P = A + v_B + v_C $$

$v_B$ is the distance of $P$ from $A$ towards $B$. So, it can be rewritten as $w_B * (B-A)$, where $w_B$ is an unknown scalar and $(B-A)$ is the difference in position between $A$ and $B$. Similarly, $v_C$ can be rewritten as $w_C * (C-A)$. So the equation can be rewritten as:
$$P = A + w_B (B-A) + w_C (C-A)$$

With $w_B$ and $w_C$, it is much easier to see if $P$ is in $\Delta ABC$. If $w_B$ is less than 0 or greater than 1, that means the end point of $v_B$ (if $v_B$ starts at $A$) is not on line segment $\overline{AB}$. This means that $P$ must be outside $\Delta ABC$. This is the same for $w_C$. And $w_B + w_C$ is always greater than 1 when $P$ is on the outer side of line segment $\overline{BC}$. Therefore, $P$ is in $\Delta ABC$ only if:
- $w_B \geq 0$
- $w_C \geq 0$
- $w_B + w_C \leq 1$

To calculate $w_B$ and $w_C$, the vectors must first be expanded into their x and y components.
$$P = A + w_B (B-A) + w_C (C-A)$$

$$\therefore P_x = A_x + w_B (B_x-A_x) + w_C (C_x-A_x), P_y = A_y + w_B (B_y-A_y) + w_C (C_y-A_y)$$

By rearranging the x-position equation, $w_B$ can be made the subject, to get $w_B$ in terms of $w_C$ and known variables. 
$$P_x = A_x + w_B (B_x-A_x) + w_C (C_x-A_x)$$

$$ -w_B (B_x-A_x) = A_x + w_C (C_x-A_x) - P_x $$

$$ w_B (B_x-A_x) = P_x - A_x - w_C (C_x-A_x)$$

$$ w_B = \frac {P_x - A_x - w_C (C_x-A_x)} {B_x-A_x} $$

The fraction can be substituted into the y-position equation, replacing $w_B$. This leaves $w_C$ as the only unknown variable.

$$\because P_y = A_y + w_B (B_y-A_y) + w_C (C_y-A_y)$$

$$\therefore P_y = A_y + \frac {P_x - A_x - w_C (C_x-A_x)} {B_x-A_x} (B_y-A_y) + w_C (C_y-A_y)$$

$$ P_y (B_x-A_x) = A_y (B_x-A_x) + \big[P_x - A_x - w_C (C_x-A_x)\big] (B_y-A_y) + w_C (C_y-A_y) (B_x-A_x)$$

$$ P_y (B_x-A_x) = A_y (B_x-A_x) + (P_x - A_x) (B_y-A_y) - w_C (C_x-A_x) (B_y-A_y) + w_C (C_y-A_y) (B_x-A_x)$$

$$ w_C (C_x-A_x)(B_y-A_y) - w_C (C_y-A_y) (B_x-A_x) = A_y (B_x-A_x) + (P_x - A_x) (B_y-A_y) - P_y (B_x-A_x) $$

$$ w_C \big[(C_x-A_x) (B_y-A_y) - (C_y-A_y) (B_x-A_x)\big] = (A_y-P_y)(B_x-A_x) + (P_x - A_x) (B_y-A_y) $$

$$w_C = \frac {(A_y-P_y)(B_x-A_x) + (P_x - A_x) (B_y-A_y)} {(C_x-A_x) (B_y-A_y) - (C_y-A_y) (B_x-A_x)}$$

So $w_C$ and $w_B$ can be calculated, using these two equations:
$$w_C = \frac {(A_y-P_y)(B_x-A_x) + (P_x - A_x) (B_y-A_y)} {(C_x-A_x) (B_y-A_y) - (C_y-A_y) (B_x-A_x)}, w_B = \frac {P_x - A_x - w_C (C_x-A_x)} {B_x-A_x}$$

Divisions by zero are a problem while calculating $w_B$. To fix this problem, if $B_x-A_x = 0$, or $B_x=A_x$, the values of $B$ and $C$ must swap. However, divisions by zero with $w_C$ are not a problem since it will only happen if the triangle is degenerate (a line).

To Increase the efficiency, constants (values not affected by $P$) can be calculated beforehand so they are not re-calculated while checking multiple points (like an array of pixels). The inverse of the denominators in the fractions can also be pre-calculated into a constant, since multiplying is much more time-efficient for computers. Calculating $(C_y-A_y)$ does not make our algorithm any faster since it only appears once.
- $\Delta x_B = B_x-A_x$
- $\Delta y_B = B_y-A_y$
- $\Delta x_C = C_x-A_x$
- $W_{cDiv} = \frac {1} {\Delta x_C \Delta y_B - (C_y-A_y) \Delta x_B}$
- $W_{bDiv} = \frac {1} {\Delta x_B}$

Using these constants, the equations for $w_C$ and $w_B$ can be rewritten as:

$$w_C = \big[ (A_y-P_y) \Delta x_B + (P_x-A_x) \Delta y_B \big] * W_{cDiv} $$

$$w_B = (P_x - A_x - w_C * x_C) * W_{bDiv}$$

In conclusion, the algorithm to find every pixel in a triangle is:
1. create a rectangle that encloses the triangle, using the minimum and maximum values of the x and y position of $\Delta ABC$. Every point in $\Delta ABC$ is in this rectangle.
2. check if $B_x = A_x$. If this is true, then swap the values of $B$ and $C$. This is to avoid division by zero in step 4.
3. precalculate constants $\Delta x_B$, $\Delta y_B$, and $\Delta x_C$.
4. use constants to calculate $W_{bDiv}$ and $W_{cDiv}$.
5. for every point, calculate its $w_B$ and $w_C$. If $w_C \geq 0$, $w_B \geq 0$, and $w_B + w_C \leq 1$, then the point is in the triangle.
