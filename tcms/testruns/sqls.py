CLONE_ENV_VALUES = '''
INSERT INTO `tcms_env_run_value_map` (run_id, value_id) VALUES %s
'''

GET_CONFIRMED_CASES = '''
SELECT
`test_cases`.`case_id`, `test_cases`.`creation_date`, `test_cases`.`summary`,
`test_case_categories`.`name` as category_name,
`priority`.`value` as priority_value, `auth_user`.`username` as author_username
FROM `test_cases`
INNER JOIN `test_case_plans` ON (`test_cases`.`case_id` = `test_case_plans`.`case_id`)
INNER JOIN `test_case_categories` ON (`test_cases`.`category_id` = `test_case_categories`.`category_id`)
INNER JOIN `priority` ON (`test_cases`.`priority_id` = `priority`.`id`)
INNER JOIN `auth_user` ON (`test_cases`.`author_id` = `auth_user`.`id`)
WHERE `test_case_plans`.`plan_id` = %s AND `test_cases`.`case_status_id` = 2
'''

STATS_CASERUNS_STATUS = '''
SELECT test_case_runs.case_run_status_id, COUNT(*) AS status_count
FROM test_case_runs
WHERE test_case_runs.run_id = %s
GROUP BY test_case_runs.case_run_status_id
'''

GET_RUN_BUG_IDS = '''
SELECT test_case_bugs.bug_id, test_case_bug_systems.url_reg_exp
FROM test_case_bugs
INNER JOIN test_case_runs ON (test_case_bugs.case_run_id = test_case_runs.case_run_id)
INNER JOIN test_case_bug_systems ON (test_case_bugs.bug_system_id = test_case_bug_systems.id)
WHERE test_case_runs.run_id = %s
'''

GET_CASERUNS_BUGS = '''
SELECT test_case_runs.case_run_id,
    test_case_bugs.bug_id,
    test_case_bug_systems.url_reg_exp
FROM test_case_runs
INNER JOIN test_case_bugs
    ON (test_case_runs.case_run_id = test_case_bugs.case_run_id)
INNER JOIN test_case_bug_systems
    ON (test_case_bugs.bug_system_id = test_case_bug_systems.id)
WHERE test_case_runs.run_id = %s
ORDER BY test_case_runs.case_run_id
'''

GET_BUG_COUNT = '''
select count(distinct test_case_bugs.bug_id) from test_case_bugs
inner join test_case_runs on (test_case_bugs.case_run_id = test_case_runs.case_run_id)
where test_case_runs.run_id = %s
'''
