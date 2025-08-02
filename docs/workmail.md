# Amazon WorkMail in InboxBrain
## 1. What is Amazon WorkMail and how is it used in this project?
Amazon WorkMail is a cloud-based, managed business email and calendar service provided by AWS. It allows you to create and manage mailboxes, calendars, and contacts, accessible from standard email clients or the web.

In this project, Amazon WorkMail serves as the user-facing entry point for incoming emails. Any message sent to the configured WorkMail account triggers an automated workflow that extracts, analyzes, and processes its contents using serverless AWS components.

## 2. Creating the WorkMail Organiztion
To set up Amazon WorkMail for InboxBrain, follow these steps:
1. Go to Amazon WorkMail in the AWS Console.
2. Click “Create organization.”
3. Organization settings:
   You’ll be prompted to configure the organization’s domain settings. You have several options:
   - Existing Route 53 domain: Choose a domain name that you already manage using Route 53.
   - New Route 53 domain: Register a new domain through Route 53 directly in AWS.
   - External domain: Enter a domain name that you manage using an external DNS provider.
   - Free test domain: Select the free testing domain provided by Amazon WorkMail. This is the easiest option for initial setup, testing, or proof-of-concept deployments. You can add a real domain later if needed.

4. Alias:
Enter an alias that will be used in your email address, e.g. inboxbrain, to create an address like `<user>@inboxbrain.awsapps.com`.

5. Finish and wait:
Complete the creation process. AWS will provision the organization and set up the selected domain. This may take a few minutes.

**Tip: For most projects and initial testing, the free test domain is sufficient and requires no DNS configuration.**

## 3. Creating Users and Mailboxes
After the organization is ready:
- Navigate to the “Users” section within your WorkMail organization.
- Click “Add user” to create new mailboxes.
- Choose a descriptive user name (alias) that matches your project goals. For example: `assistant@inboxbrain.awsapps.com`.
- Multiple mailboxes can be created if you need to separate workflows or environments.
- Each user gets login credentials for webmail or third-party email clients.
