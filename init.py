from auth_account import ApplicationSession

try:
    _ = ApplicationSession()
except SystemExit:
    quit()
