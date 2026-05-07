````markdown
# Lazy Admin - TryHackMe Walkthrough

## Room Information

| Room | Difficulty | Platform |
|------|-------------|-----------|
| Lazy Admin | Easy | TryHackMe |

---

# Introduction

Lazy Admin is an easy Linux machine focused on:
- Enumeration
- CMS exploitation
- Reverse shell access
- Linux privilege escalation

This room demonstrates how exposed backup files and insecure configurations can lead to full system compromise.

---

# Enumeration

I started with an Nmap scan to identify open ports and services.

```bash
nmap -sV <TARGET-IP>
````

## Open Ports

* **22** → SSH
* **80** → Apache HTTP Server

The website displayed the default Apache page, so I proceeded with directory enumeration using Gobuster.

```bash
gobuster dir -u http://<TARGET-IP> -w /usr/share/wordlists/dirb/common.txt
```

## Interesting Directory Found

```text
/content
```

---

# Discovering SweetRice CMS

Browsing `/content` revealed that the target was running **SweetRice CMS**.

I performed another Gobuster scan against the new directory.

```bash
gobuster dir -u http://<TARGET-IP>/content -w /usr/share/wordlists/dirb/common.txt
```

## Directories Found

```text
/as
/inc
```

* `/as` → Login panel
* `/inc` → Application files

---

# Finding Backup Files

Inside `/inc`, I discovered:

```text
/content/inc/mysql_backup
```

A downloadable SQL backup file was available.

After downloading and inspecting the SQL dump, I found administrator credentials.

The password was stored as an MD5 hash.

## Hash Cracking

Tools used:

* hash-identifier
* john
* crackstation

After cracking the hash, I obtained valid CMS admin credentials.

---

# CMS Login

Using the recovered credentials, I logged into:

```text
/content/as
```

This provided access to the SweetRice admin dashboard.

---

# Remote Code Execution

Inside the admin dashboard, the **Ads** section allowed file uploads.

I downloaded the PHP reverse shell from PentestMonkey and modified:

* attacker IP
* listening port

Then I uploaded the shell.

## Start Listener

```bash
nc -lvnp 4444
```

After accessing the uploaded shell through the browser, I received a reverse shell connection.

---

# Shell Stabilization

To improve shell interaction:

```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

---

# User Flag

After obtaining shell access:

```bash
cat user.txt
```

---

# Privilege Escalation

I checked sudo permissions.

```bash
sudo -l
```

The output showed that a Perl script could be executed as root without a password.

The script executed:

```text
/etc/copy.sh
```

After checking permissions, I discovered the file was writable.

I modified the script with a reverse shell payload and started another listener.

Then I executed the vulnerable Perl script.

```bash
sudo /usr/bin/perl /home/itguy/backup.pl
```

This triggered a root shell connection.

---

# Root Access

Verify privileges:

```bash
whoami
```

Output:

```text
root
```

Retrieve the root flag:

```bash
cat /root/root.txt
```

---

# Skills Learned

* Nmap Enumeration
* Directory Bruteforcing
* CMS Enumeration
* SQL Backup Analysis
* Hash Cracking
* Reverse Shells
* Linux Privilege Escalation

---

# Conclusion

This room demonstrated how:

* exposed backup files,
* weak password storage,
* insecure CMS configurations,
* and dangerous sudo permissions

can result in full server compromise.

A great beginner-friendly room for practicing web exploitation and Linux privilege escalation.

---

```
```
