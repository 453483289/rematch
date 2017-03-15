from .identity_hash import IdentityHashMatch
from .name_hash import NameHashMatch
from .assembly_hash import AssemblyHashMatch
from .mnemonic_hash import MnemonicHashMatch
from .mnemonic_hist import MnemonicHistogramMatch


match_list = [IdentityHashMatch, NameHashMatch, AssemblyHashMatch,
              MnemonicHashMatch, MnemonicHistogramMatch]

__all__ = ['IdentityHashMatch', 'NameHashMatch', 'AssemblyHashMatch',
           'MnemonicHashMatch', 'MnemonicHistogramMatch', 'match_list']
