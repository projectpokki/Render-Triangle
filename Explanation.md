On a 2d plane, the position of a point $P$ relative to a triangle $\Delta ABC$ can be represented by 3 vectors:
- $A$, a vertex of $\Delta ABC$
- $v_B$, a vector parallel to $\overline{AB}$
- $v_C$ is a vector parallel to $\overline{AC}$

Using these vectors, the position of $P$ can be represented as:
$$P = A + v_B + v_C $$

$v_B$ is the distance of $P$ from $A$ towards $B$. So, it can be rewritten as $w_B * (B-A)$, where $w_B$ is an unknown scalar and $(B-A)$ is the difference in position between $A$ and $B$. Similarly, $v_C$ can be rewritten as $w_C * (C-A)$. So the equation can be rewritten as:
$$P = A + w_B (B-A) + w_C (C-A)$$

With $w_B$ and $w_C$, it is much easier to see if $P$ is in $\Delta ABC$. $P$ must be outside $\Delta ABC$ if $w_B$ or $w_C$ is greater than 1 or less than 0. And if $P$ is outside of the triangle where $\overline{BC}$ is between itself and $A$, then $w_B + w_C > 1$. This means $P$ is inside $\Delta ABC$ only if all these requirements are true:
- $0 \leq w_B \leq 1$
- $0 \leq w_C \leq 1$
- $w_B + w_C \leq 1$

To calculate $w_B$ and $w_C$, the vectors must first be expanded into their x and y components. For now, the x component is all that is needed.
$$P = A + w_B (B-A) + w_C (C-A)$$

$$\therefore P_x = A_x + w_B (B_x-A_x) + w_C (C_x-A_x), P_y = A_y + w_B (B_y-A_y) + w_C (C_y-A_y)$$

Then, by rearranging the x-position equation, $w_B$ can be made the subject, to get $w_B$ in terms of $w_C$ and known variables. 
$$P_x = A_x + w_B (B_x-A_x) + w_C (C_x-A_x)$$

$$ -w_B (B_x-A_x) = A_x + w_C (C_x-A_x) - P_x $$

$$ w_B (B_x-A_x) = P_x - A_x - w_C (C_x-A_x)$$

$$ w_B = \frac {P_x - A_x - w_C (C_x-A_x)} {B_x-A_x} $$

Then, the fraction can be substituted into the y-position equation, replacing $w_B$.

DO THE MATH <!!!>
