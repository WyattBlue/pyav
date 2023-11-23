import errno
import traceback

import av

from .common import TestCase, is_windows


class TestErrorBasics(TestCase):
    def test_stringify(self):
        for cls in (av.ValueError, av.FileNotFoundError, av.DecoderNotFoundError):
            e = cls(1, "foo")
            self.assertEqual(f"{e}", "[Errno 1] foo")
            self.assertEqual(f"{e!r}", f"{cls.__name__}(1, 'foo')")
            self.assertEqual(
                traceback.format_exception_only(cls, e)[-1],
                f"av.error.{cls.__name__}: [Errno 1] foo\n",
            )

        for cls in (av.ValueError, av.FileNotFoundError, av.DecoderNotFoundError):
            e = cls(1, "foo", "bar.txt")
            self.assertEqual(f"{e}", "[Errno 1] foo: 'bar.txt'")
            self.assertEqual(f"{e!r}", f"{cls.__name__}(1, 'foo', 'bar.txt')")
            self.assertEqual(
                traceback.format_exception_only(cls, e)[-1],
                f"av.error.{cls.__name__}: [Errno 1] foo: 'bar.txt'\n",
            )

    def test_bases(self):
        self.assertTrue(issubclass(av.ValueError, ValueError))
        self.assertTrue(issubclass(av.ValueError, av.FFmpegError))

        self.assertTrue(issubclass(av.FileNotFoundError, FileNotFoundError))
        self.assertTrue(issubclass(av.FileNotFoundError, OSError))
        self.assertTrue(issubclass(av.FileNotFoundError, av.FFmpegError))

    def test_filenotfound(self):
        """Catch using builtin class on Python 3.3"""
        try:
            av.open("does not exist")
        except FileNotFoundError as e:
            self.assertEqual(e.errno, errno.ENOENT)
            if is_windows:
                self.assertTrue(
                    e.strerror
                    in ["Error number -2 occurred", "No such file or directory"]
                )
            else:
                self.assertEqual(e.strerror, "No such file or directory")
            self.assertEqual(e.filename, "does not exist")
        else:
            self.fail("no exception raised")

    def test_buffertoosmall(self):
        """Throw an exception from an enum."""
        try:
            av.error.err_check(-av.error.BUFFER_TOO_SMALL.value)
        except av.BufferTooSmallError as e:
            self.assertEqual(e.errno, av.error.BUFFER_TOO_SMALL.value)
        else:
            self.fail("no exception raised")
