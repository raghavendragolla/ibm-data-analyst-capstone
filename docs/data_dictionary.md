# Data Dictionary: IBM Data Analyst Capstone Project

This dictionary defines all attributes in the primary Developer Survey dataset (`data/raw/m1_survey_data.csv`), based on the official 2019 Stack Overflow Developer Survey schema.

---

## 1. Primary Survey Schema (`m1_survey_data.csv`)

| Column Name | Data Type | Missing Count (Raw) | Missing % | Description |
| :--- | :--- | :--- | :--- | :--- |
| `Respondent` | `int64` | 0 | 0.00% | Unique randomized identifier assigned to each survey respondent. |
| `MainBranch` | `str` | 0 | 0.00% | Primary professional identity (e.g., professional developer, student). |
| `Hobbyist` | `str` | 0 | 0.00% | Whether respondent codes as a hobby outside of work (Yes/No). |
| `OpenSourcer` | `str` | 0 | 0.00% | Frequency of contributing to open source projects. |
| `OpenSource` | `str` | 81 | 0.70% | Perception of open source software quality vs. proprietary. |
| `Employment` | `str` | 0 | 0.00% | Employment status (e.g., Full-time, Part-time). |
| `Country` | `str` | 0 | 0.00% | Country in which respondent currently resides. |
| `Student` | `str` | 53 | 0.46% | Current student enrollment status (No, Full-time, Part-time). |
| `EdLevel` | `str` | 116 | 1.00% | Highest level of formal education completed. |
| `UndergradMajor` | `str` | 740 | 6.41% | Undergraduate academic major / field of study. |
| `EduOther` | `str` | 164 | 1.42% | Non-degree educational sources utilized (bootcamps, online courses). |
| `OrgSize` | `str` | 98 | 0.85% | Number of employees in respondent's company/organization. |
| `DevType` | `str` | 67 | 0.58% | Developer roles held by respondent (semicolon-delimited list). |
| `YearsCode` | `str` | 9 | 0.08% | Total years writing code (including education and hobby). |
| `Age1stCode` | `str` | 13 | 0.11% | Age when respondent wrote their first line of code. |
| `YearsCodePro` | `str` | 16 | 0.14% | Years coding professionally in employment. |
| `CareerSat` | `str` | 0 | 0.00% | Self-reported career satisfaction level. |
| `JobSat` | `str` | 1 | 0.01% | Self-reported current job satisfaction level. |
| `MgrIdiot` | `str` | 498 | 4.31% | Perception of direct manager's competence. |
| `MgrMoney` | `str` | 502 | 4.35% | Perception of compensation fairness vs. manager. |
| `MgrWant` | `str` | 498 | 4.31% | Desire to transition into management. |
| `JobSeek` | `str` | 0 | 0.00% | Current job search / employment seeking status. |
| `LastHireDate` | `str` | 0 | 0.00% | Recency of last job search or hire date. |
| `LastInt` | `str` | 423 | 3.66% | Nature of interview process for current role. |
| `FizzBuzz` | `str` | 37 | 0.32% | Whether asked to solve classic coding challenge during hiring. |
| `JobFactors` | `str` | 3 | 0.03% | Priorities considered when evaluating a job offer. |
| `ResumeUpdate` | `str` | 41 | 0.35% | Reason for most recent resume update. |
| `CurrencySymbol` | `str` | 0 | 0.00% | Currency symbol for respondent's compensation. |
| `CurrencyDesc` | `str` | 0 | 0.00% | Full currency name and ISO code. |
| `CompTotal` | `float64` | 815 | 7.06% | Raw reported total annual, monthly, or weekly compensation. |
| `CompFreq` | `str` | 206 | 1.78% | Compensation reporting frequency (Yearly, Monthly, Weekly). |
| `ConvertedComp` | `float64` | 822 | 7.12% | Annualized compensation in USD (calculated via exchange rate). |
| `WorkWeekHrs` | `float64` | 125 | 1.08% | Average working hours per week reported. |
| `WorkPlan` | `str` | 123 | 1.06% | Structuredness of daily/weekly work planning. |
| `WorkChallenge` | `str` | 168 | 1.45% | Primary obstacles and challenges encountered at work. |
| `WorkRemote` | `str` | 8 | 0.07% | Remote work frequency and policies. |
| `WorkLoc` | `str` | 32 | 0.28% | Primary working location (Office, Home, Other). |
| `ImpSyn` | `str` | 5 | 0.04% | Self-assessed competence vs. peers (imposter syndrome indicator). |
| `CodeRev` | `str` | 1 | 0.01% | Participation in formal code review processes. |
| `CodeRevHrs` | `float64` | 2,469 | 21.37% | Average hours spent per week performing code reviews. |
| `UnitTests` | `str` | 29 | 0.25% | Whether unit testing is standard practice at respondent's organization. |
| `PurchaseHow` | `str` | 198 | 1.71% | Degree of purchasing influence for technology/tools. |
| `PurchaseWhat` | `str` | 38 | 0.33% | Types of tools respondent purchases or recommends. |
| `LanguageWorkedWith` | `str` | 11 | 0.10% | Programming languages used actively in past year (semicolon list). |
| `LanguageDesireNextYear` | `str` | 137 | 1.19% | Programming languages desired to work with next year. |
| `DatabaseWorkedWith` | `str` | 456 | 3.95% | Databases used actively in past year (semicolon list). |
| `DatabaseDesireNextYear` | `str` | 1,055 | 9.13% | Databases desired to work with next year. |
| `PlatformWorkedWith` | `str` | 422 | 3.65% | Platforms/Cloud environments used actively (semicolon list). |
| `PlatformDesireNextYear` | `str` | 561 | 4.86% | Platforms/Cloud environments desired next year. |
| `WebFrameWorkedWith` | `str` | 1,413 | 12.23% | Web frameworks used actively in past year. |
| `WebFrameDesireNextYear` | `str` | 1,634 | 14.14% | Web frameworks desired next year. |
| `MiscTechWorkedWith` | `str` | 2,209 | 19.12% | Other libraries/tools used (e.g., Node.js, Pandas, Unity). |
| `MiscTechDesireNextYear` | `str` | 1,474 | 12.76% | Other libraries/tools desired next year. |
| `DevEnviron` | `str` | 29 | 0.25% | Primary development environments / IDEs (semicolon list). |
| `OpSys` | `str` | 34 | 0.29% | Primary desktop operating system used for development. |
| `Containers` | `str` | 82 | 0.71% | Containerization technology usage (Docker, Kubernetes). |
| `BlockchainOrg` | `str` | 2,354 | 20.38% | Organization's adoption of blockchain technologies. |
| `BlockchainIs` | `str` | 2,637 | 22.83% | Attitude toward blockchain technology utility. |
| `BetterLife` | `str` | 100 | 0.87% | Belief whether technologies are making life better. |
| `ITperson` | `str` | 35 | 0.30% | Perception of self as the family IT support person. |
| `OffOn` | `str` | 38 | 0.33% | Frequency of 'have you tried turning it off and on again'. |
| `SocialMedia` | `str` | 301 | 2.61% | Most used social media platform. |
| `Extraversion` | `str` | 20 | 0.17% | Personality trait self-assessment (introversion/extraversion). |
| `ScreenName` | `str` | 513 | 4.44% | Username handle privacy preference. |
| `SOVisit1st` | `str` | 325 | 2.81% | First exposure / visit to Stack Overflow. |
| `SOVisitFreq` | `str` | 5 | 0.04% | Frequency of visiting Stack Overflow. |
| `SOVisitTo` | `str` | 1 | 0.01% | Primary purpose for visiting Stack Overflow. |
| `SOFindAnswer` | `str` | 3 | 0.03% | Success rate finding answers on Stack Overflow. |
| `SOTimeSaved` | `str` | 51 | 0.44% | Estimated time saved using Stack Overflow. |
| `SOHowMuchTime` | `str` | 1,936 | 16.76% | Hours spent on Stack Overflow per week. |
| `SOAccount` | `str` | 1 | 0.01% | Whether respondent has a registered Stack Overflow account. |
| `SOPartFreq` | `str` | 1,148 | 9.94% | Frequency of asking, answering, or participating on SO. |
| `SOJobs` | `str` | 6 | 0.05% | Usage of Stack Overflow Jobs for career discovery. |
| `EntTeams` | `str` | 5 | 0.04% | Usage of Stack Overflow for Teams. |
| `SOComm` | `str` | 0 | 0.00% | Sense of community belonging on Stack Overflow. |
| `WelcomeChange` | `str` | 89 | 0.77% | Perception of Stack Overflow welcomingness. |
| `SONewContent` | `str` | 1,995 | 17.27% | Perception of new content value on Stack Overflow. |
| `Age` | `float64` | 297 | 2.57% | Respondent's chronological age in years. |
| `Gender` | `str` | 75 | 0.65% | Self-identified gender identity. |
| `Trans` | `str` | 123 | 1.06% | Whether respondent identifies as transgender. |
| `Sexuality` | `str` | 547 | 4.74% | Self-identified sexual orientation. |
| `Ethnicity` | `str` | 683 | 5.91% | Self-identified racial or ethnic background. |
| `Dependents` | `str` | 144 | 1.25% | Whether respondent has financial dependents. |
| `SurveyLength` | `str` | 19 | 0.16% | Perception of survey questionnaire length. |
| `SurveyEase` | `str` | 14 | 0.12% | Perception of survey question clarity and ease. |

---

## 2. Job Postings Schema (`data/raw/jobs.json`)

| Field Name | Data Type | Missing Count | Description |
| :--- | :--- | :--- | :--- |
| `Id` | `integer` | 0 | Unique identifier for the job posting record. |
| `Job Title` | `string` | 0 | Advertised job title (e.g., 'Data Analyst', 'Python Developer'). |
| `Job Experience Required` | `string` | 0 | Required years of professional experience bracket. |
| `Key Skills` | `string` | 0 | Pipe- or comma-delimited required technical skills and technologies. |
| `Role Category` | `string` | 0 | Functional category within the hiring organization. |
| `Location` | `string` | 0 | City or metropolitan area of the job opportunity. |
| `Functional Area` | `string` | 0 | Business vertical (IT Software, Marketing, Analytics, etc.). |
| `Industry` | `string` | 0 | Industry sector of the hiring firm. |
| `Role` | `string` | 0 | Specific organizational role. |

---

## 3. Programming Languages Benchmark (`data/raw/Programming_Languages.html`)

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| `No.` | `integer` | Benchmark rank identifier (1 to 10). |
| `Language` | `string` | Programming language name. |
| `Created By` | `string` | Original creator / designer of the language. |
| `Average Annual Salary` | `string (currency)` | Baseline annual compensation benchmark. |
| `Learning Difficulty` | `string` | Categorical difficulty level (Easy, Hard, Difficult). |
