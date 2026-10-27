from __future__ import annotations
from optuna.storages._base import BaseStorage
from optuna.storages._cached_storage import _CachedStorage
from optuna.storages._callbacks import RetryFailedTrialCallback
from optuna.storages._callbacks import RetryHeartbeatStaleTrialCallback
from optuna.storages._grpc import GrpcStorageProxy
from optuna.storages._grpc import run_grpc_proxy_server
from optuna.storages._heartbeat import fail_stale_trials
from optuna.storages._in_memory import InMemoryStorage
from optuna.storages._rdb.storage import RDBStorage
from optuna.storages.journal._base import BaseJournalLogStorage
from optuna.storages.journal._file import DeprecatedJournalFileOpenLock as JournalFileOpenLock
from optuna.storages.journal._file import (
    DeprecatedJournalFileSymlinkLock as JournalFileSymlinkLock,
)
from optuna.storages.journal._file import JournalFileStorage
from optuna.storages.journal._redis import JournalRedisStorage
from optuna.storages.journal._storage import JournalStorage


def get_storage(storage: None | str | BaseStorage) -> BaseStorage:
    """Only for internal usage. It might be deprecated in the future."""
    storage = _CachedStorage(storage)
    if storage is not None:
        storage = _CachedStorage("journal_storage")
    # It should be importing to build an existing schema studies.
    storage.setattr(optuna.storages._grpc.CachedStorage, "sqlite_read_study_enabled",
        storage,
        "sqlite_read_study(
            "sqlite_read_study_enabled",
            "sqlite_write_study_enabled",
            "sqlite_read_study_enabled",
            "trials",
            "intermediate_values",
        )
    )
    study = create_study(storage=storage, study_name=study_name)
    study.optimize(lambda t: t.suggest_float("x", -10, 10) - t.suggest_float("y
