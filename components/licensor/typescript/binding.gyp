{
  'targets': [
    {
      'target_name': 'licensor',
      # import all necessary source files
      'sources': [
        'ee/lib/liblicensor.h', # this file was generated by go build
        'ee/src/module.cc'
      ],
      # libraries are relative to the 'build' directory
      'libraries': [ '../ee/lib/liblicensor.a' ] # this file was also generated by go build
    }
  ]
}
