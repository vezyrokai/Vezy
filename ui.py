from config import APP_NAME, VERSION

def banner():
    print(r"""
██╗   ██╗███████╗███████╗██╗   ██╗
╚██╗ ██╔╝██╔════╝╚══███╔╝╚██╗ ██╔╝
 ╚████╔╝ █████╗    ███╔╝  ╚████╔╝
  ╚██╔╝  ██╔══╝   ███╔╝    ╚██╔╝
   ██║   ███████╗███████╗   ██║
   ╚═╝   ╚══════╝╚══════╝   ╚═╝""")
    print(f"              {APP_NAME} v{VERSION}")
    print("       Passive reconnaissance | Python")
    print("-" * 54)

def section(title):
    print("\n" + "=" * 54)
    print(f" {title.upper()}")
    print("=" * 54)

def pause():
    input("\nPress Enter to return to menu...")
