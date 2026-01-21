# Testing Guide: Space Pioneers API Rebrand

This document provides a comprehensive testing checklist to verify the rebrand from "Human Spaceflight API" to "Space Pioneers API" before merging.

## Quick Test (5 minutes)

### 1. Start the Application

**Option A: Using Docker (Recommended)**
```bash
docker-compose up --build
```

**Option B: Local Development**
```bash
python manage.py runserver
```

### 2. Visual Verification Checklist

Open your browser and verify the following:

#### Homepage: http://localhost:8000
- [ ] Browser tab title shows "Home | Space Pioneers API"
- [ ] Logo in navbar shows "Space Pioneers API" text (or updated logo)
- [ ] Main heading reads "Space pioneers data" (not "Human spaceflight data")
- [ ] Footer shows "spacepioneersapi.com"
- [ ] Footer contact email shows "info@spacepioneersapi.com"
- [ ] Copyright notice shows "Copyright © 2026 Space Pioneers API. All rights reserved."

#### Navigation Pages
- [ ] **Astronauts List** (http://localhost:8000/astronauts/) - Title: "Astronauts | Space Pioneers API"
- [ ] **Agencies List** (http://localhost:8000/agencies/) - Title: "Agencies | Space Pioneers API"
- [ ] **Missions List** (http://localhost:8000/missions/) - Title: "Missions | Space Pioneers API"
- [ ] **EVAs List** (http://localhost:8000/evas/) - Title: "EVAs | Space Pioneers API"
- [ ] **Crew List** (http://localhost:8000/missions/crew/) - Title: "Crew Members | Space Pioneers API"

#### Authentication Pages
- [ ] **Login** (http://localhost:8000/accounts/login/) - Title: "Login | Space Pioneers API"
- [ ] **Signup** (http://localhost:8000/accounts/signup/) - Title: "Signup | Space Pioneers API"
- [ ] **Password Reset** (http://localhost:8000/accounts/password/reset/) - Title: "Reset Password | Space Pioneers API"

#### Error Pages (if accessible)
- [ ] **404 Page** - Title: "404: Page not found | Space Pioneers API"
- [ ] **500 Page** - Title: "500: Server Error | Space Pioneers API"
- [ ] **403 Page** - Title: "403: Forbidden | Space Pioneers API"

### 3. Logo File Check

Verify logo files are accessible:
```bash
# Check if new logo files exist
ls -la static/base/images/spacepioneersapi-navbarlogotext.svg
ls -la static/base/images/spacepioneers-navbarlogotext.svg

# Check if old logo files are gone
ls -la static/base/images/humanspaceflightapi-navbarlogotext.svg  # Should not exist
ls -la static/base/images/humanspaceflight-navbarlogotext.svg     # Should not exist
```

Expected: New files exist, old files do not.

---

## Comprehensive Test (15-30 minutes)

### 1. Code Verification

#### Search for Old References
```bash
# This should return ONLY the CHANGELOG.md and README.md (contextual mentions)
grep -ri "human spaceflight" --exclude-dir=.git --exclude="*.md" .

# This should return no results
grep -ri "humanspaceflightapi" --exclude-dir=.git --exclude="*.md" .

# Verify new branding is present (should find many files)
grep -ri "Space Pioneers API" --exclude-dir=.git .
```

Expected Results:
- No old branding in code files (only in .md documentation)
- New branding appears throughout templates and config

#### Check Logo References
```bash
# Verify base.html references the new logo
grep "spacepioneersapi-navbarlogotext.svg" templates/base.html
```

Expected: Should find the reference.

### 2. Functional Testing

#### Test Database Migration (if applicable)
```bash
# Check for any pending migrations
python manage.py showmigrations

# Run migrations if needed
python manage.py migrate

# Verify no issues
echo $?  # Should output 0 (success)
```

#### Test Static Files Collection
```bash
# Collect static files
python manage.py collectstatic --noinput

# Verify logo files are collected
ls -la staticfiles/base/images/spacepioneersapi-navbarlogotext.svg  # Should exist
```

#### Run Django Test Suite (if tests exist)
```bash
# Run all tests
python manage.py test

# Or run with verbose output
python manage.py test --verbosity=2
```

### 3. Browser Testing

#### Multi-Page Navigation Test
1. Start from homepage
2. Click each navigation link (Astronauts, Agencies, Missions, EVAs)
3. Verify each page:
   - Shows correct title in browser tab
   - Shows new logo in navbar
   - Shows updated footer
   - No console errors (press F12 to check Developer Tools)

#### Detail Page Test (if data exists)
1. Navigate to a list page (e.g., Astronauts)
2. Click on an individual item
3. Verify detail page title includes "| Space Pioneers API"

#### Form Submission Test
1. Try logging in (or creating an account)
2. Verify form pages show new branding
3. Check confirmation/error pages for correct branding

### 4. Mobile Responsiveness Check

Test on different screen sizes:
- Desktop (1920px)
- Tablet (768px)
- Mobile (375px)

Verify:
- [ ] Logo displays correctly at all sizes
- [ ] Footer remains readable
- [ ] Navigation collapses appropriately

### 5. Cross-Browser Testing

Test in multiple browsers:
- [ ] Chrome/Chromium
- [ ] Firefox
- [ ] Safari (if on Mac)
- [ ] Edge

---

## Automated Testing Script

Save this as `test_rebrand.sh`:

```bash
#!/bin/bash

echo "========================================="
echo "Space Pioneers API Rebrand Test Script"
echo "========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test 1: Check for old branding in code
echo "Test 1: Checking for old branding in code files..."
OLD_BRAND=$(grep -ri "humanspaceflight" --exclude-dir=.git --exclude="*.md" --exclude="TESTING_REBRAND.md" . 2>/dev/null | wc -l)
if [ "$OLD_BRAND" -eq 0 ]; then
    echo -e "${GREEN}✓ PASS: No old branding found in code files${NC}"
else
    echo -e "${RED}✗ FAIL: Found $OLD_BRAND instances of old branding${NC}"
    grep -ri "humanspaceflight" --exclude-dir=.git --exclude="*.md" --exclude="TESTING_REBRAND.md" .
fi
echo ""

# Test 2: Check for new branding
echo "Test 2: Checking for new branding..."
NEW_BRAND=$(grep -ri "Space Pioneers API" --exclude-dir=.git . 2>/dev/null | wc -l)
if [ "$NEW_BRAND" -gt 20 ]; then
    echo -e "${GREEN}✓ PASS: Found $NEW_BRAND instances of new branding${NC}"
else
    echo -e "${RED}✗ FAIL: Only found $NEW_BRAND instances (expected >20)${NC}"
fi
echo ""

# Test 3: Check logo files
echo "Test 3: Checking logo files..."
if [ -f "static/base/images/spacepioneersapi-navbarlogotext.svg" ]; then
    echo -e "${GREEN}✓ PASS: New logo file exists (spacepioneersapi)${NC}"
else
    echo -e "${RED}✗ FAIL: New logo file missing${NC}"
fi

if [ ! -f "static/base/images/humanspaceflightapi-navbarlogotext.svg" ]; then
    echo -e "${GREEN}✓ PASS: Old logo file removed (humanspaceflightapi)${NC}"
else
    echo -e "${YELLOW}⚠ WARNING: Old logo file still exists${NC}"
fi
echo ""

# Test 4: Check base.html logo reference
echo "Test 4: Checking base.html logo reference..."
if grep -q "spacepioneersapi-navbarlogotext.svg" templates/base.html; then
    echo -e "${GREEN}✓ PASS: base.html references new logo${NC}"
else
    echo -e "${RED}✗ FAIL: base.html doesn't reference new logo${NC}"
fi
echo ""

# Test 5: Check copyright year
echo "Test 5: Checking copyright year..."
if grep -q "2026 Space Pioneers API" templates/base.html; then
    echo -e "${GREEN}✓ PASS: Copyright year updated to 2026${NC}"
else
    echo -e "${YELLOW}⚠ WARNING: Copyright year may not be updated${NC}"
fi
echo ""

# Test 6: Check config files
echo "Test 6: Checking config file docstrings..."
CONFIG_UPDATED=0
if grep -q "Space Pioneers API project" config/wsgi.py; then
    ((CONFIG_UPDATED++))
fi
if grep -q "Space Pioneers API project" config/asgi.py; then
    ((CONFIG_UPDATED++))
fi
if grep -q "Space Pioneers API project" config/settings/settings.py; then
    ((CONFIG_UPDATED++))
fi

if [ "$CONFIG_UPDATED" -eq 3 ]; then
    echo -e "${GREEN}✓ PASS: All config files updated${NC}"
else
    echo -e "${YELLOW}⚠ WARNING: Only $CONFIG_UPDATED/3 config files updated${NC}"
fi
echo ""

# Summary
echo "========================================="
echo "Test Summary"
echo "========================================="
echo "Manual testing still required:"
echo "  1. Run the application and verify visually"
echo "  2. Test all navigation links"
echo "  3. Check browser console for errors"
echo "  4. Test on mobile devices"
echo ""
```

Make it executable and run:
```bash
chmod +x test_rebrand.sh
./test_rebrand.sh
```

---

## Known Issues to Check

### Potential Problems
1. **Static Files Not Loading**
   - Solution: Run `python manage.py collectstatic`

2. **Logo Not Displaying**
   - Check: Browser dev tools (F12) → Network tab
   - Verify: 404 errors for logo files
   - Solution: Clear browser cache, restart server

3. **Old Branding Still Visible**
   - Solution: Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
   - Clear browser cache
   - Check if running old Docker containers

### CSS/JS Issues
- Clear browser cache
- Check console for 404 errors
- Verify static files are being served correctly

---

## Sign-off Checklist

Before merging the rebrand, confirm:

- [ ] All automated tests pass
- [ ] Visual inspection shows new branding throughout
- [ ] No old logo files remain
- [ ] No "Human Spaceflight API" text in code (except documentation)
- [ ] README.md is comprehensive and accurate
- [ ] CHANGELOG.md documents the changes
- [ ] All navigation links work
- [ ] No console errors in browser
- [ ] Footer shows correct domain and email
- [ ] Copyright year is 2026
- [ ] Logo displays correctly
- [ ] Mobile view is functional

---

## Rollback Plan (if needed)

If issues are found after merge:

```bash
# Revert the commit
git revert <commit-hash>

# Or reset to previous commit (use with caution)
git reset --hard <previous-commit-hash>
git push --force-with-lease origin claude/rename-space-pioneers-api-tB49y
```

**Note**: Only force push to feature branches, never to main/master!
