
## Add Local Scripts to Your PATH

Sometimes when you install Python packages, you may see a warning that says scripts were installed in a folder that is “not on PATH”.

To prevent this warning and make those tools work, run these two commands:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### What this does

- It permanently adds the folder `~/.local/bin` to your PATH.
- This is the folder where `pip` sometimes places extra tools.
- After running these commands, those tools will be found automatically.