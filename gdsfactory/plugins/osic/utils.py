"""
Essential integration functions between OpenLane2 and GDSFactory are included here.
Read further under `docs/openlane_integration`:

.. include:: ../docs/plugins_openlane.md
"""
import os
import shutil
import pathlib
import openlane


def copy_source_folder(source_directory: str, target_directory: str) -> None:
    """
    Copies a design directory
    Args:
        source_directory(str): Source directory PATH.
        target_directory(str): Target directory PATH.

    Returns:
        None

    """
    if os.path.exists(target_directory):
        answer = input("Confirm deletion of: " + target_directory)
        if answer.upper() in ["Y", "YES"]:
            shutil.rmtree(target_directory)
        elif answer.upper() in ["N", "NO"]:
            print(
                "Copying files now from: "
                + source_directory
                + " to "
                + target_directory
            )

    shutil.copytree(
        source_directory,
        target_directory,
        symlinks=False,
        ignore=None,
        copy_function=shutil.copy2,
        ignore_dangling_symlinks=False,
        dirs_exist_ok=False,
    )


def setup_default_example(target_directory: str = "/foss/designs/spm") -> None:
    """
    Sets up the OpenLane default SPM design. You need to copy the example run file.

    Args:
        target_directory:

    Returns:
        None

    """
    openlane_directory = pathlib.Path(openlane.__file__).parent.resolve()
    openlane_default_example_directory = openlane_directory / "smoke_test_design/"
    copy_source_folder(
        source_directory=str(openlane_default_example_directory),
        target_directory=target_directory,
    )


__all__ = ["setup_default_example"]
