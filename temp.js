;(function () {
  'use strict'
  angular
    .module('wdpr.wdprAngularCore.config')
    .constant('environment', 'production')
    .constant('packageName', 'wdpr-web-dcl-homepage')
    .constant('angularConfig', {
      localizedAnalytics: { wdw: ['en_GB', 'en-eu'], dlr: [], dcl: [] },
      globalMessageKey: 'url',
      personalizationDecisionUrl:
        '/wam/recommendation-service/personalized-content',
      useWamBaseURLForAuth: false,
      vpgEnableRules: {
        siteId: ['wdw'],
        geo: { countryisocode: ['us'] },
        preferredLanguage: ['en-us', 'en_US'],
        locale: ['en_US']
      },
      vpgWamBaseURL: '/wam/vpg',
      wamBaseURL: '/api/wdpro',
      finderWamBaseURL: '/api/wdpro',
      togglesFile: {
        dlr: '/i18n/wdpr-ui-universal-layout/dlr/toggles.json',
        wdw: '/i18n/wdpr-ui-universal-layout/wdw/toggles.json'
      },
      contentURL: {
        dlr: 'https://secure.cdn1.wdpromedia.com/media/flashComponents/content-backup/dlr/{lang}/content.json',
        wdw: 'https://secure.cdn1.wdpromedia.com/media/flashComponents/content-backup/wdw/{lang}/content.json'
      },
      videoCdnBaseUrl: 'https://cdn1.parksmedia.wdprapps.disney.com',
      appConfig: { defaultSeasonId: 'any-season' },
      protectedEnabled: false,
      cdnBaseUrls: [
        'https://cdn2.parksmedia.wdprapps.disney.com/media/dcl/pipeline',
        'https://cdn2.parksmedia.wdprapps.disney.com/media/dcl/pipeline',
        'https://cdn2.parksmedia.wdprapps.disney.com/media/dcl/pipeline',
        'https://cdn2.parksmedia.wdprapps.disney.com/media/dcl/pipeline',
        'https://cdn2.parksmedia.wdprapps.disney.com/media/dcl/pipeline'
      ],
      consoleLevel: 1,
      apiLevel: 1
    })
  angular.module('wdpr.personalization').constant('p13nSiteConfig', {
    p13nsitedata: {
      configuration: {
        CEA: {
          SessionIdCookieJarName: 'causata_jar',
          SessionIdCookieName: 'id',
          authCookieIncludeSubDomains: 'true',
          authTimeout: '2500',
          captureTimeout: '2500',
          captureURL: '/wam/recommendation-service/personalization-events',
          debug: { remoteLogUri: '/utils/log' },
          decisionTimeout: '500',
          decisionURL: '/wam/recommendation-service/personalized-content',
          enableTrackElementLinkTracking: 'true',
          personalizationIdCookieJarName: 'personalization_jar',
          personalizationIdCookieName: 'id',
          rules: {
            'configuration-contentLanguage': 'en',
            'configuration-contentLocale': 'us',
            guestType: 'Guest',
            storeType: 'Consumer'
          },
          turnOff: 'false'
        },
        DITracking: {
          server: 'https%3A//ctologger01.qa.media.data.disney.com/cto',
          turnOff: 'false'
        },
        Dart: {
          advertiserId: '2789293',
          defaultConditions: [{ contentLanguage: 'en', contentLocale: 'us' }]
        },
        DerbySoft: { turnOff: 'false' },
        GoogleHotels: { turnOff: 'false' },
        GoogleRemarketing: { turnOff: 'false' },
        Omni: { csrfSelector: '#pep_csrf', turnOff: 'false' },
        SiteCatalyst: { reportSuiteId: 'wdgwdprowdw' },
        TestAndTarget: { globalMbox: 'true' },
        TripAdvisor: { turnOff: 'false' },
        contentLanguage: 'en',
        contentLocale: 'us',
        sreka: 'true',
        trackingTimeoutMilliseconds: '550',
        environment: 'PROD'
      },
      contentTests: [
        {
          contentPosition: 'append',
          contentTestHTMLTargetElement: 'body',
          contentTestModuleName: 'target-global-mbox'
        },
        {
          contentPosition: 'append',
          contentTestHTMLTargetElement: 'body',
          contentTestModuleName: 'WDW_GlobalNav_ThingsToDoAndPlacesToStay',
          contentTestTriggerElement:
            '.syndicated-section.syndicated-section--thingsToDo,.syndicated-section.syndicated-section--placesToStay',
          contentTestTriggerEvent: 'mouseover',
          contentTestTriggerEventBindType: 'one'
        },
        {
          contentPosition: 'append',
          contentTestHTMLTargetElement: 'body',
          contentTestModuleName: 'WDW_Global2'
        }
      ],
      location: { city: 'Orlando', country: 'USA', region: 'Florida' },
      pageKeyLocations: {
        finder_details_type_attractions: [
          {
            alterationMethod: { desktop: 'prepend', mobile: 'after' },
            clickSelector: 'section.ctaContainer.blueStyle a',
            contentKey: 'descriptions.ctaDarkBlue.text',
            impressionType: 'visible',
            location: 'wdw-site-pzn-cta1',
            locationShortName: 'L35',
            selector:
              '.finderDetailsContentRight,.finderDetailsContent h2.finderDetailsPageSubtitle'
          },
          {
            alterationMethod: 'after',
            clickSelector: 'section.ctaContainer.lightBlueStyle a',
            contentKey: 'descriptions.ctaLightBlue.text',
            domReadyTimeout: '250',
            impressionType: 'visible',
            location: 'wdw-site-pzn-cta2',
            locationShortName: 'L36',
            selector: 'section.ctaContainer.blueStyle'
          }
        ],
        finder_details_type_dining: [
          {
            alterationMethod: 'replaceContent',
            contentKey: 'descriptions.atAGlance.text',
            impressionType: 'visible',
            location: 'wdw-site-pzn-diningdetail-ataglance-dineplan',
            locationShortName: 'L33',
            selector: '.diningPlansAcceptedText'
          }
        ],
        finder_details_type_entertainment: [
          {
            alterationMethod: 'replaceWith',
            clickSelector: 'section.ctaContainer a',
            contentKey: 'descriptions.ctaDarkBlue.text',
            impressionType: 'visible',
            location: 'wdw-site-pzn-cta1',
            locationShortName: 'L35',
            selector: '#showInPlansCTA'
          },
          {
            alterationMethod: 'after',
            clickSelector: 'section.ctaContainer.lightBlueStyle a',
            contentKey: 'descriptions.ctaLightBlue.text',
            domReadyTimeout: '250',
            impressionType: 'visible',
            location: 'wdw-site-pzn-cta2',
            locationShortName: 'L36',
            selector: '#showInPlansCTA,section.ctaContainer.blueStyle'
          }
        ]
      },
      personalizations: [
        {
          additionalMBox: 'WDW_LoginRedirect_Mbox',
          impressionType: 'immediate',
          location: 'wdpr-wdw-o-nav-login',
          locationShortName: 'L1',
          serverSide: 'true'
        },
        {
          alterationMethod: 'replaceWith',
          clickSelector:
            '.syndicated-section--thingsToDo .syndicated-flyout__secondary .syndicated-link-groups__list--promo li:nth-child(2) a',
          contentKey: {
            desktop: 'descriptions.globalNavSubmenuCopyPC.text',
            mobile: 'descriptions.globalNavSubmenuCopyMobile.text'
          },
          impressionEvent: 'mouseenter',
          impressionSelector: '.syndicated-section--thingsToDo',
          impressionType: 'customEvent',
          location: 'wdw-site-pzn-globalnavbar-thingstodo-rightsubmenu02',
          locationShortName: 'L2',
          selector:
            '.syndicated-section--thingsToDo .syndicated-flyout__secondary .syndicated-link-groups__list--promo li:nth-child(2)'
        },
        {
          alterationMethod: 'replaceWith',
          clickSelector:
            '.syndicated-section--placesToStay .syndicated-flyout__secondary .syndicated-link-groups__list--promo li:nth-child(3) a',
          contentKey: {
            desktop: 'descriptions.globalNavSubmenuCopyPC.text',
            mobile: 'descriptions.globalNavSubmenuCopyMobile.text'
          },
          impressionEvent: 'mouseenter',
          impressionSelector: '.syndicated-section--placesToStay',
          impressionType: 'customEvent',
          location: 'wdw-site-pzn-globalnavbar-placestostay-rightsubmenu03',
          locationShortName: 'L3',
          selector:
            '.syndicated-section--placesToStay .syndicated-flyout__secondary .syndicated-link-groups__list--promo li:nth-child(3)'
        },
        {
          decisionOnly: 'true',
          location: 'wdpr-wdw-o-analytics-vpc',
          locationShortName: 'L55',
          locationType: 'data'
        }
      ],
      site: 'WDW',
      activationRules: {
        contentLocale: 'en_US',
        countryisocode: 'us',
        siteId: 'wdw'
      },
      p13nLocations: {
        global: {
          'wdw-site-pzn-globalnavbar-placestostay-rightsubmenu03': '1',
          'wdw-site-pzn-globalnavbar-thingstodo-rightsubmenu02': '1'
        },
        'wdw-site-homepage': {
          'wdw-site-pzn-globalnavbar-placestostay-rightsubmenu03': {
            alterationMethod: 'replaceWith',
            contentKey: 'descriptions.globalNavSubmenuCopyPC.text',
            domReadyTimeout: '5000',
            selector:
              '.syndicated-section--placesToStay .syndicated-flyout__secondary .syndicated-link-groups__list--promo li:nth-child(3)'
          },
          'wdw-site-pzn-globalnavbar-thingstodo-rightsubmenu02': {
            alterationMethod: 'replaceWith',
            contentKey: 'descriptions.globalNavSubmenuCopyPC.text',
            domReadyTimeout: '5000',
            selector:
              '.syndicated-section--thingsToDo .syndicated-flyout__secondary .syndicated-link-groups__list--promo li:nth-child(2)'
          },
          'wdw-site-pzn-homepage-revenuemodule-left': {
            alterationMethod: 'html',
            contentKey: 'text',
            selector:
              'story-block-group[p13n-location=wdw-site-pzn-homepage-revenuemodule-left]'
          },
          'wdw-site-pzn-homepage-revenuemodule-right': {
            alterationMethod: 'html',
            contentKey: 'text',
            selector:
              'story-block-group[p13n-location=wdw-site-pzn-homepage-revenuemodule-right]'
          },
          'wdw-site-pzn-upsell-type': { alterationMethod: 'orderElements' }
        }
      },
      pageId: 'NA',
      siteSection: 'NA'
    }
  })
})()
