# Snyk Badges -- Examples for Secure Developer GitHub Repos
---> [![Known Vulnerabilities](https://snyk.io/test/github/snyk-labs/secure-developer-sample-repo/badge.svg)](https://snyk.io/test/github/snyk-labs/secure-developer-sample-repo) <---


Your repo on GitHub can contain badges reflecting Snyk scan results. The scan can occur on the built package on NPM, PyPi, or other platforms; or it can scan the code on GitHub directly. This repo contains some vulnerabilities deliberately. It contains:

* Vulnerable `app.py` for SAST / code scanning demonstration
* Manifest file `requirements.txt` containing outdated (vulnerable) versions of packages
* Terraform files to demonstrate Snyk IaC scanning

Try clicking on the badge at the top of this README to see the [full scan results](https://snyk.io/test/github/snyk-labs/secure-developer-sample-repo) for this demo codebase.

Open source projects can join Snyk's [Secure Developer Program](https://snyk.io/open-source/) to obtain access to Enterprise security features for free. One of the few requirements for joining the program is to include a reference to Snyk in your project's README. The badges shown off in this demo repo are all valid ways of doing that. You can also/alternatively use the PNG badges at the bottom of this demo README.

## Setting up badges for public repositories
### Step 1: Create a Snyk account

1. Navigate to https://snyk.io and click "Sign up" (it will be free)
2. Choose GitHub OAuth for easier integration
3. Authorize Snyk to access your GitHub account

### Step 2: Import your GitHub repository

1. In Snyk dashboard, go to `Integrations → Source Control → GitHub Snyk` 

![alt text](documentation_images/image.png)

2. Click "Add your GitHub repositories to Snyk". You may need to grant Snyk some additional permissions:

![alt text](documentation_images/image-1.png)

3. Select the repositories you want to monitor (you can search for them by name)

![alt text](documentation_images/image-2.png)

4. Wait for initial vulnerability scan to complete (usually 1-2 minutes)

5. If your repo does not have any code yet, now would be a good time to add some. This repo contains some deliberately vulnerable code in `app.py`.
![alt text](documentation_images/image-4.png)

6. If you do not have a manifest file, you'll want to configure one appropriate for your project. A manifest file is just a file from your language that is standard for indicating your dependencies. If you want Open Source dependency scanning, you’ll need at least one of the supported manifests:

`Python → requirements.txt, Pipfile, or pyproject.toml`

`Node.js → package.json`

`Java → pom.xml or build.gradle`

This repository contains a `requirements.txt` file with some deliberately outdated dependencies to show off vulnerability scanning.
![alt text](documentation_images/image-3.png)

7. The natural next step would be to set up GitHub Actions with Snyk. You can explore some options for this [here](https://github.com/snyk/actions). But for now, you've done enough to create your badge(s).

## GitHub Badges
For a scan that is configured to scan your code on an open source GitHub repo directly:

Basic GitHub badge:
```
[![Known Vulnerabilities](https://snyk.io/test/github/{username}/{repo}/badge.svg)](https://snyk.io/test/github/{username}/{repo})
```

In our case:
```
[![Known Vulnerabilities](https://snyk.io/test/github/snyk-labs/secure-developer-sample-repo/badge.svg)](https://snyk.io/test/github/snyk-labs/secure-developer-sample-repo)
```

Which comes out looking like this:
[![Known Vulnerabilities](https://snyk.io/test/github/snyk-labs/secure-developer-sample-repo/badge.svg)](https://snyk.io/test/github/snyk-labs/secure-developer-sample-repo)

Or for specific branch:
```
[![Known Vulnerabilities](https://snyk.io/test/github/{username}/{repo}/{branch}/badge.svg)](https://snyk.io/test/github/{username}/{repo}/{branch})
```

Targeting a specific manifest file (if you have a monorepo with multiple `requirements.txt` files, for example):
```
[![Known Vulnerabilities](https://snyk.io/test/github/{username}/{repo}/badge.svg?targetFile=package.json)](https://snyk.io/test/github/{username}/{repo}?targetFile=package.json)
```

Using custom styling:
```
[![Known Vulnerabilities](https://snyk.io/test/github/{username}/{repo}/badge.svg?style=flat-square)](https://snyk.io/test/github/{username}/{repo})
```

An example combining these parameters:
```
[![Known Vulnerabilities](https://snyk.io/test/github/{username}/{repo}/badge.svg?targetFile=package.json&style=flat-square)](https://snyk.io/test/github/{username}/{repo}?targetFile=package.json)
```

## NPM Package Badges
For a scan that is configured to scan your code on NPM:


Basic npm badge:
```
[![Known Vulnerabilities](https://snyk.io/test/npm/{package-name}/badge.svg)](https://snyk.io/test/npm/{package-name})
```

Specific version:
```
[![Known Vulnerabilities](https://snyk.io/test/npm/{package-name}/{version}/badge.svg)](https://snyk.io/test/npm/{package-name}/{version})
```

## PyPI package badges
For a scan that is configured to scan your code on PyPi:

Basic PyPi badge:
```
[![Known Vulnerabilities](https://snyk.io/test/pip/{package-name}/badge.svg)](https://snyk.io/test/pip/{package-name})
```

## Maven Central badges
For a scan that is configured to scan your code on Maven Central:
Basic Maven badge:
```
[![Known Vulnerabilities](https://snyk.io/test/maven/{groupId}/{artifactId}/badge.svg)](https://snyk.io/test/maven/{groupId}/{artifactId})
```

## PHP Composer badges
For a scan that is configured to scan your code on PHP Composer:

Basic PHP badge:
```
[![Known Vulnerabilities](https://snyk.io/test/composer/{vendor}/{package}/badge.svg)](https://snyk.io/test/composer/{vendor}/{package})
```

## PNG Badges

### Reduced Size (25%):


<!-- <img src="Secure%20Developer%20Badge%20Full%20%283%29.png" alt="Secure Developer Badge" width="10%" style="display: inline-block; margin-right: 10px;"><img src="secure_developer_program_round.png" alt="Secure Developer Program Round" width="10%" style="display: inline-block;"> -->
<img src="Scanned_By_Snyk.png" alt="Scanned By Snyk Badge" width="25%" style="display: inline-block;">

### Full Size:


<!-- ![Secure Developer Badge](Secure%20Developer%20Badge%20Full%20%283%29.png)
![Secure Developer Program Round](secure_developer_program_round.png) -->
![Scanned by Snyk Badge](Scanned_By_Snyk.png)

## SVG Badges

### Reduced Size (10%):


<img src="badge_full.svg" alt="Secure Developer Badge Full" width="10%" style="display: inline-block; margin-right: 10px;"><img src="badge_round.svg" alt="Secure Developer Program Round" width="10%" style="display: inline-block;">

### Full Size:


![Secure Developer Badge Full](badge_full.svg)
![Secure Developer Program Round](badge_round.svg)