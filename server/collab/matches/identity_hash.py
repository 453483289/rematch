from . import hash_match


class IdentityHashMatch(hash_match.HashMatch):
  vector_type = 'identity_hash'
  match_type = 'identity_hash'
