"""Read-only public-package checks; no network or installation."""
import json, re, sys
from validate_paper import ROOT, read_json, check_state

def audit(root=ROOT):
    errors=[]
    required=['SKILL.md','README.md','LICENSE.md','START_HERE.md','CORE_SPEC.md','WORKFLOW.md','UNIVERSAL_PROMPT.md','PAPER_SCHEMA.json','QA_CHECKLIST.md','PLATFORM_GUIDE.md','state/STARTER_STATE.json','scripts/validate_paper.py','scripts/render_print.py','scripts/migrate_state.py','scripts/migrate_paper.py','references/cyclic-authoring-loop.md','references/writing-visual-rotation.md']
    for name in required:
        if not (root/name).is_file():errors.append('missing: '+name)
    for path in root.rglob('*.md'):
        if '.git' in path.parts:continue
        for link in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
            if '://' in link or link.startswith('#'):continue
            target=link.split('#')[0]
            if target and not (path.parent/target).exists():errors.append('broken link: '+str(path.relative_to(root))+': '+target)
    try:errors.extend(check_state(read_json(root/'state/STARTER_STATE.json')))
    except (OSError,ValueError) as ex:errors.append(str(ex))
    if sys.version_info<(3,10):errors.append('Python 3.10+ required')
    return {'status':'FAIL' if errors else 'PASS','errors':errors,'not_verified':['source truth','answer uniqueness','independent review','PDF layout','exam equivalence']}
if __name__=='__main__':
    result=audit();print(json.dumps(result,ensure_ascii=False,indent=2));sys.exit(bool(result['errors']))
