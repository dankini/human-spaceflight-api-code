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
OLD_BRAND=$(grep -ri "humanspaceflight" --exclude-dir=.git --exclude="*.md" --exclude="*.sh" . 2>/dev/null | wc -l)
if [ "$OLD_BRAND" -eq 0 ]; then
    echo -e "${GREEN}✓ PASS: No old branding found in code files${NC}"
else
    echo -e "${RED}✗ FAIL: Found $OLD_BRAND instances of old branding${NC}"
    grep -ri "humanspaceflight" --exclude-dir=.git --exclude="*.md" --exclude="*.sh" .
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
