from pathlib import Path

documents_dir = Path.cwd() / "practice_files" / "documents"

images_dir = Path.home() / "images"
images_dir.mkdir(exist_ok = True)

for path in documents_dir.rglob("*.*"):
    if path.suffix.lower() in [".png", ".jpg", ".gif"]:
        path.replace(images_dir / path.name)