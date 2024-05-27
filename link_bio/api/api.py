import link_bio.styles.constants as ct

async def live(user:str) -> bool:
    if user == "ukory_":
        return True
    else:
        return False
    
async def repo() -> str:
    return "https://github.com/Jhanfer/link-bio-page"