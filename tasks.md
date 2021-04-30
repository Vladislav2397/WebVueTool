# Tasks

- [ ] Create classes
    - [x] **File**
    - [ ] **Directory** ?
    - [x] **ListComponents**
- [ ] Optimize code
- [ ] Create view
    - [x] table
    

### File:
- properties
    - name -> str
    - suffix -> str
    - extension -> str
    - content -> Union[str|list]
    - filename -> str
    - parent -> Path
    - full path -> Path

- methods
    - find -> str
    - exists -> bool
    - write -> None
    - create -> None
    - remove -> None

### Component
- private vars
    - vue file -> File
    - main file -> File
    - critical file -> File
    - type -> Path

- properties
    - name -> str
    - class name -> str
    - functional -> str
    - is style -> bool
    - type -> Path

- methods
    - create -> None
    - remove -> None
    
### ListComponent
- properties
    - items
