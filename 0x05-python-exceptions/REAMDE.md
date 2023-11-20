HANDLING EXCEPTIONS
The try..except statement works as follows.

First, the try clause (the statement(s) between the try and except keywords) is executed.
If no exception occurs, the except clause is skipped and execution of the try statement is finished.
If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block.
If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.

The except clause(s) specify one or more exception handlers. When no exception occurs in the try clause, no exception handler is executed. When an exception occurs in the try suite, a search for an exception handler is started. This search inspects the except clauses in turn until one is found that matches the exception. An expression-less except clause, if present, must be last; it matches any exception. For an except clause with an expression, that expression is evaluated, and the clause matches the exception if the resulting object is “compatible” with the exception. An object is compatible with an exception if the object is the class or a non-virtual base class of the exception object, or a tuple containing an item that is the class or a non-virtual base class of the exception object.
