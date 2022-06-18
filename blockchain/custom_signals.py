from django import dispatch

reject_withdrawal = dispatch.Signal()

approve_withdrawal = dispatch.Signal()

withdrawal = dispatch.Signal()