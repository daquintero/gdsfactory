from __future__ import annotations

import gdsfactory as gf
from gdsfactory.components.die import die
from gdsfactory.typings import Component, ComponentFactory

_cols_200mm_wafer = (2, 6, 6, 8, 8, 6, 6, 2)


@gf.cell
def wafer(
    reticle: ComponentFactory = die,
    cols: tuple[int, ...] = _cols_200mm_wafer,
    xspacing: float | None = None,
    yspacing: float | None = None,
    die_name_col_row: bool = False,
) -> Component:
    """Returns complete wafer. Useful for mask aligner steps.

    Args:
        reticle: spec for each wafer reticle.
        cols: how many columns per row.
        xspacing: optional spacing, defaults to reticle.xsize.
        yspacing: optional spacing, defaults to reticle.ysize.
        die_name_col_row: if True, die name is row_col, otherwise is a number
    """
    c = gf.Component()
    die = reticle()
    xspacing = xspacing or die.d.xsize
    yspacing = yspacing or die.d.ysize

    i = 1
    for col in range(len(cols)):
        for row in range(cols[col]):
            die_name = f"{col+1}_{row+1}" if die_name_col_row else str(i)
            die = reticle(die_name=die_name)
            ref = c.add_ref(die)
            ref.d.movex((row - cols[col] / 2) * xspacing)
            ref.d.movey(col * yspacing)
            i += 1

    return c


if __name__ == "__main__":
    c = wafer(die_name_col_row=True)
    c.show()
