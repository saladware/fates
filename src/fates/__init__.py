"""fates — A generic Result[T, E] type for explicit error propagation."""

from fates._async import AsyncResult as AsyncResult
from fates._err import AsyncErr as AsyncErr
from fates._err import Err as Err
from fates._exc import UnwrapError as UnwrapError
from fates._ok import AsyncOk as AsyncOk
from fates._ok import Ok as Ok
from fates._result import Result as Result
