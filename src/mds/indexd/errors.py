# Auth Errors
class AuthError(Exception):
    """
    Base auth error.
    """


class AuthzError(Exception):
    """
    Base authz error.
    """


class UserError(Exception):
    """
    User error.
    """


# Base Errors
class ConfigurationError(Exception):
    """
    Configuration error.
    """


class IndexdUnexpectedError(Exception):
    """
    Unexpected Error
    """

    def __init__(self, code=500, message="Unexpected Error"):
        self.code = code
        self.message = str(message)


class BaseIndexError(Exception):
    """
    Base index error.
    """


class NoRecordFound(BaseIndexError):
    """
    No record error.
    """


# Index Errors
class MultipleRecordsFound(BaseIndexError):
    """
    Multiple recordss error.
    """


class RevisionMismatch(BaseIndexError):
    """
    Revision mismatch.
    """


class UnhealthyCheck(BaseIndexError):
    """
    Health check failed.
    """


class AddExistedColumn(BaseIndexError):
    """
    Existed column error.
    """


class AddExistedTable(BaseIndexError):
    """
    Existed table error.
    """
