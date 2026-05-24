# Test Strategy

## Objective
Build a scalable automation framework combining:
- UI testing
- API testing
- Integration testing
- CI execution
- Reporting

## Platform/URL used for testing
- https://www.saucedemo.com/ (UI)
- https://restful-booker.herokuapp.com (API)
- Strong community support
- Flexible architecture

## Coverage Included

### UI
- Login flow
- Dashboard interaction


### API
- CRUD validation
- Status code validation
- Response-time assertions
- Error handling

### Integration
- API + UI combined flow

### Reporting
- reports/report.html
- Screenshot on UI test failure

## Key Risks
1. No retry strategy yet
2. Logging not fully implemented yet

## Mitigations
- Explicit waits
- Externalized test data
- Stable locators

## Next Improvements
- Retry Strategy
- Parallel execution
- Better Logging
- Config-driven environment switching