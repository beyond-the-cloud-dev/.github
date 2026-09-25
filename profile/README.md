<div align="center">
  <a href="https://beyondthecloud.dev">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/logo-white.png">
      <img alt="Beyond The Cloud" src="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/logo-dark.png" height="96">
    </picture>
  </a>

  <h3>We fix the Salesforce orgs nobody wants to touch.</h3>

  <p>Senior-only team from Poland. The tools we build on client work end up here, open source.</p>

  <a href="https://beyondthecloud.dev">Website</a> &nbsp;·&nbsp;
  <a href="https://apexfluently.beyondthecloud.dev">Apex Fluently</a> &nbsp;·&nbsp;
  <a href="https://blog.beyondthecloud.dev/blog">Blog</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/company/beyondtheclouddev">LinkedIn</a> &nbsp;·&nbsp;
  <a href="https://www.youtube.com/@BeyondTheCloudDev">YouTube</a> &nbsp;·&nbsp;
  <a href="mailto:contact@beyondthecloud.dev">contact@beyondthecloud.dev</a>
</div>

<br>

### <a href="https://apexfluently.beyondthecloud.dev"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/libs/apex-fluently-white.png"><img src="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/libs/apex-fluently-dark.png" height="24" alt=""></picture></a> Apex Fluently

Open source Apex libraries we use on every client project. MIT, free, no signup.

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="200">
        <a href="https://soql.beyondthecloud.dev"><img src="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/libs/soql-lib.png" width="48" height="48" alt=""><br><b>SOQL Lib</b></a><br>
        <sub>Query builder, selectors</sub>
      </td>
      <td align="center" valign="top" width="200">
        <a href="https://dml.beyondthecloud.dev"><img src="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/libs/dml-lib.png" width="48" height="48" alt=""><br><b>DML Lib</b></a><br>
        <sub>Unit of work you can mock</sub>
      </td>
      <td align="center" valign="top" width="200">
        <a href="https://async.beyondthecloud.dev"><img src="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/libs/async-lib.png" width="48" height="48" alt=""><br><b>Async Lib</b></a><br>
        <sub>Queueable, batch, schedule</sub>
      </td>
      <td align="center" valign="top" width="200">
        <a href="https://httpmock.beyondthecloud.dev"><img src="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/libs/http-mock-lib.png" width="48" height="48" alt=""><br><b>HTTP Mock Lib</b></a><br>
        <sub>Callout mocks in one line</sub>
      </td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td align="center" valign="top" width="200">
        <a href="https://apexconsts.beyondthecloud.dev"><img src="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/libs/apex-consts.png" width="48" height="48" alt=""><br><b>Apex Consts</b></a><br>
        <sub>No more magic strings</sub>
      </td>
      <td align="center" valign="top" width="200">
        <a href="https://cachemanager.beyondthecloud.dev"><img src="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/libs/cache-manager.png" width="48" height="48" alt=""><br><b>Cache Manager</b></a><br>
        <sub>One API for Platform Cache</sub>
      </td>
      <td align="center" valign="top" width="200">
        <a href="https://testlib.beyondthecloud.dev"><img src="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/libs/test-lib.png" width="48" height="48" alt=""><br><b>Test Lib</b></a><br>
        <sub>Test data builders</sub><br>
        <sub><i>beta</i></sub>
      </td>
      <td align="center" valign="top" width="200">
        <a href="https://trigger.beyondthecloud.dev"><img src="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/libs/trigger-lib.png" width="48" height="48" alt=""><br><b>Trigger Lib</b></a><br>
        <sub>Trigger framework</sub><br>
        <sub><i>in progress</i></sub>
      </td>
    </tr>
  </tbody>
</table>

```apex
Account acme = (Account) SOQL.of(Account.SObjectType)
    .with(Account.Id, Account.Name)
    .whereAre(SOQL.Filter.with(Account.Name).equal('Acme'))
    .mockId('Acme')
    .toObject();

new DML()
    .toInsert(new Contact(LastName = 'Doe', AccountId = acme.Id))
    .identifier('NewContact')
    .commitWork();
```

In a unit test, mock both. No records, no database:

```apex
SOQL.mock('Acme').thenReturn(new Account(Name = 'Acme'));
DML.mock('NewContact').allInserts();
```

Also: [LWC Utils](https://github.com/beyond-the-cloud-dev/lwc-utils) and [VS Code snippets](https://marketplace.visualstudio.com/items?itemName=BeyondTheCloud.salesforce-snippets-beyondthecloud).

### Products

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="200">
        <a href="https://veles.beyondthecloud.dev"><img src="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/products/veles.png" width="48" height="48" alt=""><br><b>Veles</b></a><br>
        <sub>Sandbox and scratch org setup</sub>
      </td>
      <td align="center" valign="top" width="200">
        <a href="https://releasenotifier.beyondthecloud.dev"><img src="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/products/release-notifier.png" width="48" height="48" alt=""><br><b>Release Notifier</b></a><br>
        <sub>In-app release notes</sub>
      </td>
    </tr>
  </tbody>
</table>

### Work with us

Certified Technical Architect on delivery, no juniors on your org. We take on technical debt, Agentforce and AppExchange apps (we're a Salesforce PDO).

Want to know how we'd write Apex in your org? Read the source above, then say hi at [contact@beyondthecloud.dev](mailto:contact@beyondthecloud.dev).

<a href="https://beyondthecloud.dev">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/salesforce-partner.png">
    <img src="https://raw.githubusercontent.com/beyond-the-cloud-dev/.github/docs/profile-readme/assets/salesforce-partner-solid.png" height="40" alt="Salesforce Partner">
  </picture>
</a>
