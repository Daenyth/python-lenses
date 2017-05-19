from ..const import Const
from .traversals import collect_args, multiap
from .base import Fold

class IterableFold(Fold):
    '''A fold that can get values from any iterable object in python by
    iterating over it. Like any fold, you cannot set values.

        >>> IterableFold()
        IterableFold()
        >>> IterableFold().to_list_of({2, 1, 3})
        [1, 2, 3]
        >>> def numbers():
        ...     yield 1
        ...     yield 2
        ...     yield 3
        ...
        >>> IterableFold().to_list_of(numbers())
        [1, 2, 3]
        >>> IterableFold().to_list_of([])
        []

    If you want to be able to set values as you iterate then look into
    the EachTraversal.
    '''

    def func(self, f, state):
        items = list(state)
        if items == []:
            return f.pure(state)

        collector = collect_args(len(items))
        applied = multiap(collector, *map(f, items))
        return applied

    def __repr__(self):
        return 'IterableFold()'
