# Auto-Folder-Cleaner 🚀

An automated desktop utility written in Python designed to batch-clean and organize messy Windows directories. This script eliminates digital clutter by dynamically scanning multiple file ecosystems, creating type-specific directories based on file extensions, and seamlessly migrating loose files into their new sorted homes.

---

## 🛠️ Key Features

* **Batch Processing:** Accepts multiple file directory paths separated by commas to clean several folders in a single execution.
* **Dynamic Environment Setup:** Automatically detects unique file extensions present in a directory and generates matching storage folders (e.g., `pdf`, `py`, `txt`).
* **Input Resilience:** Handles messy human inputs by stripping accidental leading or trailing whitespaces from pasted paths.
* **Safe Operations:** Implements exception handling and safety flags (`exist_ok=True`) to prevent overwriting existing folders or system crashes.

---

## 🧠 Architectural Overview & Logic Flow

The engine operates sequentially through a 4-stage pipeline when a directory path is passed to it:

1. **Path Verification:** The script uses `os.path.exists` to screen out invalid paths. If valid, it reads the target directory using `os.listdir`.
2. **Segregation:** Items are evaluated using `os.path.splitext`. Sub-folders are left alone, while actual files are isolated.
3. **Deduplication:** File extensions are extracted and processed through a Python `set` container to isolate unique file types, preventing the creation of duplicate folders.
4. **Migration:** The script maps out native absolute addresses using `os.path.join` and shifts files from their source coordinates to their destination sub-folders using `shutil.move`.

---

## 🚀 How To Run the Script

### Prerequisites
Make sure you have Python installed on your Windows machine. No external third-party libraries are required, as this engine relies entirely on built-in standard Python systems components (`os` and `shutil`).

### Terminal Execution Steps

1. Clone or download the repository into your project workspace.
2. Open your Windows **Command Prompt (CMD)** or terminal.
3. Navigate to the directory containing the script:
   ```cmd
   cd path\to\your\workspace\Auto-Folder-Cleaner
