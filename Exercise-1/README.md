# Experiment 1: Hadoop HDFS File Operations

## Aim
To perform basic file operations in Hadoop Distributed File System (HDFS).

## Objective
- To understand Hadoop HDFS.
- To create text files in Ubuntu.
- To create a directory in HDFS.
- To upload files into HDFS.
- To verify and read files stored in HDFS.

## Software Used
- Ubuntu 24.04
- Hadoop 3.4.1
- Java 11

## Input
Three text files:
- file1.txt
- file2.txt
- file3.txt

## Output
The files are uploaded successfully to HDFS and their contents are displayed.

## Files
- file1.txt
- file2.txt
- file3.txt

## Commands Used

### Create Files
```bash
echo "File 1 Content" > file1.txt
echo "File 2 Content" > file2.txt
echo "File 3 Content" > file3.txt
```

### Create HDFS Directory
```bash
hdfs dfs -mkdir /data
```

### Upload Files to HDFS
```bash
hdfs dfs -put file1.txt file2.txt file3.txt /data
```

### Verify Uploaded Files
```bash
hdfs dfs -ls /data
```

### Read a File from HDFS
```bash
hdfs dfs -cat /data/file1.txt
```

## Result
The Hadoop HDFS file operations were executed successfully. The files were created, uploaded to HDFS, verified, and read successfully.
